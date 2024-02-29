# QA Engineer - Pairing Session - Interviewer Guide
Today, you will conduct an interview with a potential QA Engineer candidate. This guide will walk you through the process, from setting up the environment to evaluating the candidate's performance.

## Before the Interview
- Familiarize yourself with the challenge requirements and the potential solution provided. This will help you evaluate the candidate's approach and solutions effectively.
- Review the S3 link to the coding challenge package: [QA Interview Challenge Zip File](https://nayya-static-assets.s3.amazonaws.com/qa-interview/6-qa-skill-eval.zip). Ensure you know what the candidate will be working with.

## During the Interview
### 1. Introduction
- Start by introducing yourself and explaining the structure of the interview.
- Set a positive and welcoming tone to make the candidate feel comfortable.

### 2. Challenge Instructions
- Inform the candidate they will be working on a coding challenge that involves validating the functionality of a web form using automated tests with Playwright (or their preferred framework).
- Direct the candidate to download the coding challenge materials from the provided S3 link: [QA Interview Challenge Zip File](https://nayya-static-assets.s3.amazonaws.com/qa-interview/6-qa-skill-eval.zip)
- Ask the candidate to share their screen as they proceed with the challenge.
### 3. Guiding the Candidate
Once the candidate has downloaded and extracted the zip file, guide them through the following steps:
#### a. Set Up the Environment
- Instruct them to locate and open the README file included within. This README contains specific instructions for setting up their environment and starting the challenge.
- Ask the candidate to open a terminal or command prompt within the extracted folder.
- Instruct them to run `npm install` to install the necessary dependencies.
- Then, have them run `npx playwright install` to ensure all required browser binaries are installed unless they're using something other than Playwright.
#### b. Understand the Challenge
- Explain that the challenge involves writing test scripts to validate a web form's input fields. The focus is on checking for both correct and incorrect data inputs and ensuring the form behaves as expected.
- Mention that they should look at the provided example test cases as a starting point but encourage them to think of additional cases that might be relevant.
### 4. Observation and Discussion
- Observe how the candidate approaches problem-solving, their coding style, and their ability to debug issues.
- Encourage the candidate to verbalize their thought process as they work through the challenge.
- Discuss their approach, asking about the choices they made and any challenges they encountered.


## What We Are Looking For
When evaluating candidates' submissions, consider the following criteria:

- Does the test script cover all specified test cases?
- Are the tests correctly identifying valid and invalid inputs as per the requirements?
- Is the code well-structured, readable, and maintainable?
- How does the candidate approach problem-solving and debugging when faced with test failures or unexpected behavior?
- Does the candidate effectively utilize the framework's capabilities for test automation (like Playwright)?
- Are edge cases and potential input variations considered and tested?

## Possible Solution
```js filename="formTest.js"
  const testCases = [
    {
      description: "Valid input fields",
      inputs: { name: "John Doe", email: "john@example.com", age: "25" },
      expectedErrors: { name: "", email: "", age: "" },
      valid: true
    },
    {
      description: "Invalid name (empty)",
      inputs: { name: "", email: "john@example.com", age: "25" },
      expectedErrors: { name: "Name is required", email: "", age: "" },
      valid: false
    },
    {
      description: "Invalid email format",
      inputs: { name: "John Doe", email: "invalidemail", age: "25" },
      expectedErrors: { name: "", email: "Email is invalid", age: "" },
      valid: false
    },
    {
      description: "Age below threshold",
      inputs: { name: "John Doe", email: "john@example.com", age: "17" },
      expectedErrors: { name: "", email: "", age: "Age must be between 18 and 99" },
      valid: false
    },
  ];

  for (const testCase of testCases) {
    console.log(`Testing case: ${testCase.description}`);

    await page.fill('#name', testCase.inputs.name);
    await page.fill('#email', testCase.inputs.email);
    await page.fill('#age', testCase.inputs.age);

    await page.click('#submitButton');

    for (const field in testCase.expectedErrors) {
      const errorMessage = testCase.expectedErrors[field];
      if (errorMessage) {
        await expect(page.locator(`#${field}Error`)).toHaveText(errorMessage);
        await expect(page.locator(`#${field}`)).toHaveClass(/invalid/);
      } else {
        if (testCase.valid) {
          await expect(page.locator(`#${field}`)).toHaveClass(/valid/);
        } else {
          await expect(page.locator(`#${field}`)).not.toHaveClass(/invalid/);
        }
      }
    }

    await page.reload();
  }

  console.log('All test cases finished.');
  await browser.close();

```
## Updates to the Repo
If you end up changing the coding challenge, you should compress the changes and upload them to `s3://nayya-static-assets/qa-interview`
