const { chromium, expect } = require('@playwright/test');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();
  
  const htmlFilePath = path.join(__dirname, 'registrationForm.html');
  
  await page.goto(`file://${htmlFilePath}`);
  
  // Your testing code here

  await browser.close();
})();
