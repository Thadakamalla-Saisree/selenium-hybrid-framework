# Selenium Hybrid Test Automation Framework

An enterprise-grade **Selenium WebDriver Hybrid Test Automation Framework** in Python, featuring Page Object Model (POM), data-driven testing, reusable utilities, configuration management, and robust logging.

---

## 🏛️ Architecture Overview

The framework follows the **Hybrid Automation Framework** design pattern:
* **UI Store (`Project/tests/uistore/`)**: Centralized repository of locators.
* **Page Objects (`Project/tests/pages/`)**: Encapsulates web elements and business actions.
* **Test Suites (`Project/tests/test_page.py`)**: Test cases and validation logic.
* **Utilities (`Project/utilities/`)**: Custom WebDriver helper methods, logging, and screenshot handlers.
* **Configuration (`Project/config/`)**: Environment settings, browser configuration, and timeouts.
* **Test Data (`Project/testdata/`)**: Data-driven inputs and test fixtures.

---

## 🛠️ Tech Stack & Dependencies
* **Language**: Python 3.11+
* **Automation Engine**: Selenium WebDriver 4
* **Design Pattern**: Page Object Model (POM) + Data-Driven
* **Target Application**: Avon Cycles E-commerce Portal

---

## 🚀 Getting Started

### 1. Setup Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Execute Test Suites
```bash
python Project/tests/test_page.py
```

---

## 👤 Author
* **Thadakamalla Saisree** ([@Thadakamalla-Saisree](https://github.com/Thadakamalla-Saisree))
