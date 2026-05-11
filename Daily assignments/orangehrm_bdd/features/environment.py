import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def before_scenario(context, scenario):
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    context.driver.quit()
