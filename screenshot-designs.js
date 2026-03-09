const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const CHROME = '/root/.cache/ms-playwright/chromium-1194/chrome-linux/chrome';

const designs = [
  { file: 'design-a-bold-patriotic.html', out: 'screenshots/design-a.png' },
  { file: 'design-b-clean-corporate.html', out: 'screenshots/design-b.png' },
  { file: 'design-c-editorial.html',       out: 'screenshots/design-c.png' },
  { file: 'design-d-minimalist.html',      out: 'screenshots/design-d.png' },
];

const base = path.resolve(__dirname);
fs.mkdirSync(path.join(base, 'screenshots'), { recursive: true });

(async () => {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 1 });

  for (const d of designs) {
    const url = 'file://' + path.join(base, d.file);
    console.log('Screenshotting', d.file);
    await page.goto(url, { waitUntil: 'networkidle0' });
    await new Promise(r => setTimeout(r, 500));
    await page.screenshot({ path: path.join(base, d.out), fullPage: true });
    console.log('  -> saved', d.out);
  }

  await browser.close();
  console.log('Done.');
})();
