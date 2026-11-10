#!/usr/bin/env node
// Screenshot a page in real time with a Chrome or Chromium that is already installed.
//
//   node shoot.mjs page.html [out-dir]
//
// Writes into out-dir (default: beside the page):
//   <name>-desktop-0s.png   1440x900, the first frame
//   <name>-desktop-3s.png   1440x900, after the entrance
//   <name>-phone.png        390x844 at 2x, after the entrance
//   <name>-still.png        1440x900 with reduced motion
// and prints console errors, failed or external requests, and horizontal overflow at 320 and 390 px.
// Exit status 1 when there are errors, network requests or overflow.
//
// Needs Node 22 or later (built-in WebSocket and fetch) and nothing else. It drives the browser
// over the DevTools protocol so the phone viewport is a true 390 px and animation runs at real speed,
// which the browser's own --screenshot flag does not give you.

import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { basename, dirname, extname, join, resolve } from 'node:path';

const [pageArg, outArg] = process.argv.slice(2);
if (!pageArg || !existsSync(pageArg)) { console.error('usage: node shoot.mjs page.html [out-dir]'); process.exit(2); }
if (typeof WebSocket === 'undefined') { console.error('needs Node 22 or later'); process.exit(2); }
const page = resolve(pageArg);
const out = resolve(outArg || dirname(page));
mkdirSync(out, { recursive: true });
const name = basename(page, extname(page));
const url = 'file://' + page;

const candidates = [
  process.env.CHROME,
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
  '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser',
  '/usr/bin/google-chrome', '/usr/bin/google-chrome-stable', '/usr/bin/chromium', '/usr/bin/chromium-browser',
  '/snap/bin/chromium', '/usr/bin/microsoft-edge',
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
].filter(Boolean);
const browser = candidates.find(p => existsSync(p));
if (!browser) { console.error('no Chrome or Chromium found; set CHROME=/path/to/browser'); process.exit(3); }

const profile = mkdtempSync(join(tmpdir(), 'shoot-'));
const proc = spawn(browser, ['--headless=new', '--remote-debugging-port=0', '--no-first-run', '--hide-scrollbars',
  '--mute-audio', `--user-data-dir=${profile}`, 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
const done = code => { try { proc.kill(); } catch {} try { rmSync(profile, { recursive: true, force: true }); } catch {} process.exit(code); };

let port = 0;
for (let i = 0; i < 100 && !port; i++) {
  await sleep(100);
  try { port = parseInt(readFileSync(join(profile, 'DevToolsActivePort'), 'utf8').split('\n')[0], 10) || 0; } catch {}
}
if (!port) { console.error('browser did not start'); done(3); }
const targets = await (await fetch(`http://127.0.0.1:${port}/json`)).json();
const ws = new WebSocket(targets.find(t => t.type === 'page').webSocketDebuggerUrl);
await new Promise((ok, no) => { ws.addEventListener('open', ok); ws.addEventListener('error', no); });

let id = 0;
const pending = new Map();
const errors = new Set();
const requests = new Set();
ws.addEventListener('message', ev => {
  const m = JSON.parse(ev.data);
  if (m.id && pending.has(m.id)) { pending.get(m.id)(m.result || {}); pending.delete(m.id); return; }
  const p = m.params || {};
  if (m.method === 'Runtime.exceptionThrown') errors.add(p.exceptionDetails.exception?.description || p.exceptionDetails.text);
  if (m.method === 'Runtime.consoleAPICalled' && p.type === 'error') errors.add(p.args.map(a => a.value ?? a.description).join(' '));
  if (m.method === 'Log.entryAdded' && p.entry.level === 'error') errors.add(p.entry.text);
  if (m.method === 'Network.requestWillBeSent' && !/^(data:|blob:|about:)/.test(p.request.url) && p.request.url !== url) requests.add(p.request.url);
});
const send = (method, params = {}) => new Promise(r => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
for (const d of ['Runtime', 'Log', 'Page', 'Network']) await send(d + '.enable');

async function view(width, height, { mobile = false, calm = false } = {}) {
  await send('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: mobile ? 2 : 1, mobile });
  await send('Emulation.setTouchEmulationEnabled', { enabled: mobile });
  await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: calm ? 'reduce' : 'no-preference' }] });
  await send('Page.navigate', { url });
  await sleep(150);
}
async function shot(label) {
  const r = await send('Page.captureScreenshot', { format: 'png' });
  const file = join(out, `${name}-${label}.png`);
  writeFileSync(file, Buffer.from(r.data, 'base64'));
  console.log(file);
}
const overflow = async () => (await send('Runtime.evaluate', {
  expression: 'Math.max(document.documentElement.scrollWidth, document.body ? document.body.scrollWidth : 0) - innerWidth',
  returnByValue: true })).result?.value ?? 0;

const wide = [];
await view(1440, 900);               await shot('desktop-0s');
await sleep(3400);                   await shot('desktop-3s');
await view(390, 844, { mobile: true }); await sleep(3500); await shot('phone');
if (await overflow() > 1) wide.push(390);
await view(320, 640, { mobile: true }); await sleep(600);
if (await overflow() > 1) wide.push(320);
await view(1440, 900, { calm: true }); await sleep(1200); await shot('still');

console.log(errors.size ? `\nconsole errors (${errors.size}):\n  ` + [...errors].join('\n  ') : '\nno console errors');
console.log(requests.size ? `network requests (${requests.size}):\n  ` + [...requests].join('\n  ') : 'no network requests');
console.log(wide.length ? `horizontal overflow at ${wide.join(' and ')} px` : 'no horizontal overflow at 390 or 320 px');
done(errors.size || requests.size || wide.length ? 1 : 0);
