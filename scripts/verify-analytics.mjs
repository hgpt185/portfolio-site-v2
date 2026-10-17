// Drive headless Chrome via CDP to verify Vercel Analytics beacon fires.
// Usage: node scripts/verify-analytics.mjs [url]
import { spawn } from 'node:child_process';
import http from 'node:http';

const URL_TO_TEST = process.argv[2] || 'https://hemeshgupta.site/';
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const PORT = 9333;
const DURATION_MS = 15000;

function httpGetJson(path) {
  return new Promise((resolve, reject) => {
    http.get({ host: '127.0.0.1', port: PORT, path }, res => {
      let body = '';
      res.on('data', c => (body += c));
      res.on('end', () => resolve(JSON.parse(body)));
    }).on('error', reject);
  });
}

async function main() {
  const chrome = spawn(CHROME, [
    `--remote-debugging-port=${PORT}`,
    '--headless=new',
    '--disable-gpu',
    '--no-first-run',
    '--disable-extensions',
    '--disable-blink-features=AutomationControlled', // make navigator.webdriver undefined
    '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    '--user-data-dir=/tmp/chrome-analytics-test',
    'about:blank',
  ], { stdio: 'ignore' });

  try {
    // wait for devtools endpoint
    let targets;
    for (let i = 0; i < 30; i++) {
      await new Promise(r => setTimeout(r, 500));
      try { targets = await httpGetJson('/json/list'); break; } catch { /* retry */ }
    }
    if (!targets) throw new Error('Chrome DevTools endpoint never came up');
    const page = targets.find(t => t.type === 'page');
    if (!page) throw new Error('No page target found');

    const ws = new WebSocket(page.webSocketDebuggerUrl);
    await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });

    let id = 0;
    const pending = new Map();
    const send = (method, params = {}) => new Promise(resolve => {
      const msgId = ++id;
      pending.set(msgId, resolve);
      ws.send(JSON.stringify({ id: msgId, method, params }));
    });

    const insightRequests = [];
    const consoleErrors = [];
    ws.onmessage = ev => {
      const msg = JSON.parse(ev.data);
      if (msg.id && pending.has(msg.id)) { pending.get(msg.id)(msg.result); pending.delete(msg.id); }
      if (msg.method === 'Network.requestWillBeSent') {
        const url = msg.params.request.url;
        if (url.includes('_vercel/insights')) {
          insightRequests.push({ method: msg.params.request.method, url });
        }
      }
      if (msg.method === 'Runtime.exceptionThrown') {
        consoleErrors.push(msg.params.exceptionDetails?.exception?.description || 'exception');
      }
      if (msg.method === 'Runtime.consoleAPICalled' && ['error', 'warning'].includes(msg.params.type)) {
        consoleErrors.push(`${msg.params.type}: ${msg.params.args.map(a => a.value ?? a.description).join(' ')}`);
      }
    };

    await send('Network.enable');
    await send('Runtime.enable');
    await send('Page.enable');
    await send('Page.navigate', { url: URL_TO_TEST });
    await new Promise(r => setTimeout(r, DURATION_MS));

    console.log('=== requests to /_vercel/insights/* ===');
    if (!insightRequests.length) console.log('(none captured)');
    insightRequests.forEach(r => console.log(`${r.method} ${r.url}`));
    const beacons = insightRequests.filter(r => r.method === 'POST');
    console.log(`\npage-view beacons (POST): ${beacons.length}`);
    console.log('script GETs:', insightRequests.filter(r => r.method === 'GET').length);
    console.log('\n=== JS errors/warnings during load ===');
    console.log(consoleErrors.length ? consoleErrors.join('\n') : '(none)');

    ws.close();
  } finally {
    chrome.kill('SIGKILL');
  }
}

main().catch(e => { console.error('TEST ERROR:', e.message); process.exit(1); });
