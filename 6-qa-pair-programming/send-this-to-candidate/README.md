# QA Engineer Interview Coding Challenge
Welcome to the QA Engineer coding challenge! This challenge is designed to evaluate your skills in writing test automation scripts using Playwright or your preferred framework. You will work on implementing test cases that validate a web form's functionality based on specific requirements.

## Getting Started
### 1. Make Sure You Are Set Up
Before you begin, ensure you have the following installed on your system:

- Node.js (LTS version recommended)
- npm (comes with Node.js)
- Google Chrome + Screen Sharing

### 2. Install Dependencies

Install the required Node.js dependencies:
```
npm install
npx playwright install
npm i -D @playwright/test
```
### 3. Review the Web Form

The web form you will be testing is located in `registrationForm.html`. You can open this file in a browser to familiarize yourself with its functionality. The form includes fields for Name, Email, and Age, and implements basic validation.

### 4. Write Your Test Script

The template for your test script is in `formTest.js.` This file contains a basic structure for a Playwright script. If you want to use something else, feel free. Your task is to implement test cases that cover the form's validation logic. Refer to the provided example test script for guidance on structuring your tests.

### 5. Run the Test Script

Execute your test script with the following command:

```
node formTest.js
```
Observe the output and the browser interactions. Ensure your test cases adequately cover the form's functionality and validation requirements.

## Challenge Overview
Your challenge is to enhance the `formTest.js` script to include comprehensive test cases for the web form. The form should:

-  **Validate Form Inputs:** Ensure the Name, Email, and Age fields are validated according to the form's rules.
- **Automate Test Cases:** Write automated tests in `formTest.js` covering a range of valid and invalid inputs.
