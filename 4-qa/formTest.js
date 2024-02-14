const { chromium, expect } = require('@playwright/test');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();
  
  await page.goto('file:///path/to/interviews/4-qa/registrationForm.html');
  
  // write tests here
})();
