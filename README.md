**Automation Framework - Selenium with Pytest**

  This repository contains a modular and scalable automation testing framework built using Selenium, Pytest, and Python.

**Project Structure**
  automation_framework_selenium_pytest
  
   objects/        # UI element locators
   pages/          # Page Object Model classes
   tests/          # Test cases
   utils/          # Utilities (helpers, config, drivers)
  requirements.txt

**Features**

 1. Page Object Model (POM) design
 2. Reusable utilities and helper functions
 3. Configurable test structure
 4. Cross-browser support (if configured)
 5. Easy test execution with Pytest

**Running Tests**

  Install dependencies:
    pip install -r requirements.txt
  
  Run tests:
    pytest -v

**Generate Allure Report**

  pytest --alluredir=allure-results
  allure serve allure-results


