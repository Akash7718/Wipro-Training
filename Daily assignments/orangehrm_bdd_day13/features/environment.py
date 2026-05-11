import os
import sys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), '..', 'screenshots')


def before_scenario(context, scenario):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{scenario.name.replace(' ', '_')}_{timestamp}.png"
        filepath = os.path.join(SCREENSHOT_DIR, filename)
        context.driver.save_screenshot(filepath)
        print(f"Screenshot saved: {filepath}")
    context.driver.quit()
