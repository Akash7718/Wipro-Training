import os
import sys
import pytest
import allure
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.path.insert(0, os.path.dirname(__file__))
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")
@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    drv = webdriver.Chrome(options=chrome_options)
    yield drv
    drv.quit()
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs(SCREENSHOT_DIR, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{item.name}_{timestamp}.png"
            filepath = os.path.join(SCREENSHOT_DIR, filename)
            driver.save_screenshot(filepath)
            allure.attach.file(
                filepath,
                name=f"Screenshot - {item.name}",
                attachment_type=allure.attachment_type.PNG,
            )
