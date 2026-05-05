import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

driver =  webdriver.Edge(service = Service("../resources/msedgedriver.exe"))

driver.get("https://www.google.com/")
time.sleep(3)

driver.get("https://www.wikipedia.org/")
time.sleep(3)

driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.back()
time.sleep(3)
driver.refresh()
time.sleep(3)

driver.quit()