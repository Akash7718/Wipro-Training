

from selenium.webdriver.edge.service import Service
#from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest_check as check

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge(service = Service("../resources/msedgedriver.exe"))
    driver.maximize_window()
    driver.get('https://www.google.com')
    yield driver
    driver.quit()

def test_ghpload(driver):
    pagetitle=driver.title
    assert pagetitle=='Google','Google Home page Not loaded'

def test_imagespageload(driver):
    driver.find_element(By.LINK_TEXT,'Images').click()
    pagetitle=driver.title
    assert pagetitle=='Google Images','Google Image page Not loaded'

def test_businesslink(driver):
    driver.find_element(By.LINK_TEXT,'Business').click()
    wait = WebDriverWait(driver,10)
    wait.until(EC.title_contains('Business'))
        # assert 'Business' in driver.title,'Business page not loaded - Title Check'
        # assert 'business' in driver.current_url,'Business url not loaded - URL Check'
    check.equal(driver.title,'Business','Business page not loaded - Title Check')
    check.is_in("business",driver.current_url,"Business page not loaded-UrL check")