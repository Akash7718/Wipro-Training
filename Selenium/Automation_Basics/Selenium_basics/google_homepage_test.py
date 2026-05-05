"""
code for working in google home page
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))        #service=Service(EdgeChromiumDriverManager().install()))
browser = input('Enter browser : ')

match(browser.lower()):
    # case 'chrome':
    #     driver=webdriver.Crome(service=Service())
    case 'edge':
        driver=webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
    case _:
        print('Unknown browser - not available. \n Execute with default edge browser.')
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

driver.get("https://www.google.com/")

pagetitle = driver.title
if pagetitle == 'Google':
    print("Google homepage loaded - Pass")
else:
    print("Google homepage not loaded - Fail")

sleep(3)

driver.quit()