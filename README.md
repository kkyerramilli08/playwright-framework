# 🎭 Playwright Automation Framework

A reusable **Playwright + Pytest automation framework** for maintainable end-to-end web application testing using the **Page Object Model**, reusable utilities, test data, and automated test execution.

## 📌 Project Overview

This framework automates end-to-end web application scenarios using Playwright and Pytest.

It is designed around reusable Page Objects and supporting utilities so that test cases remain organized, maintainable, and easy to extend.

### 🎯 Framework Focus

- Page Object Model
- Reusable test utilities
- Test data management
- Pytest fixtures and configuration
- End-to-end browser automation
- Assertions and validations
- Test execution and reporting

## 🗂️ Framework Structure

```text
playwright-framework/
├── pages/           # Page Object classes
├── tests/           # Automated test scenarios
├── utilities/       # Reusable utilities and test data helpers
├── testData/        # Test data and configuration files
├── exports/         # Generated/exported files
├── conftest.py      # Pytest fixtures and shared configuration
├── pytest.ini       # Pytest configuration
└── requirements.txt # Project dependencies
```

## ❓ Why This Framework

This framework provides a structured approach to end-to-end web automation instead of placing all automation logic inside individual test cases.

It improves maintainability, reusability, readability, and scalability by separating page actions, test scenarios, test data, utilities, and configuration.

## ⚙️ How the Framework Works

The framework follows a simple execution flow:

1. Pytest starts the test execution.
2. Shared fixtures and configuration are loaded through `conftest.py` and `pytest.ini`.
3. Test cases use Page Object classes to interact with the application.
4. Page Objects contain reusable locators and page actions.
5. Utilities provide reusable support for configuration, test data, and common operations.
6. Assertions validate the expected application behavior.
7. Pytest produces the test execution and reporting results.

## 🛠️ How to Create and Use the Framework

The framework can be created and extended using the following approach:

1. Install the project dependencies from `requirements.txt`.
2. Configure the application URL and required test settings.
3. Create Page Object classes inside the `pages/` directory.
4. Add reusable utilities inside the `utilities/` directory.
5. Create test scenarios inside the `tests/` directory.
6. Use Pytest fixtures and configuration for shared setup.
7. Execute the required test scenarios with Pytest.

## ♻️ Page Objects and Utilities Reuse

Page Objects keep locators and page-specific actions in reusable classes. Test cases call these page methods instead of duplicating browser interaction code.

Utilities provide common functionality that can be reused across multiple test scenarios. This keeps the test cases focused on business flows while common support logic remains centralized.

This structure makes it easier to add new test scenarios, update application changes in one place, and reuse existing framework components across tests.

## 🧪 E2E Scenario

The framework includes a complete end-to-end SauceDemo scenario covering:

- Login using test data from Excel
- Product selection
- Cart navigation
- Checkout
- User information entry
- Order completion
- Return to the application home page

### 📄 E2E Test Script

The E2E scenario is implemented in:

`tests/test_E2EScenario_new.py`

### ▶️ Run the E2E Test

```bash
pytest tests/test_E2EScenario_new.py -v
```

### 📊 Test Output


The E2E scenario completed successfully with **1 passed test**.

## 🔑 Key Takeaway

This framework demonstrates how Playwright and Pytest can be combined with Page Objects, reusable utilities, test data, fixtures, and configuration to build a maintainable end-to-end automation framework.
