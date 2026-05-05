
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service





driver =  webdriver.Edge(service = Service("../resources/msedgedriver.exe"))

driver.get("https://www.google.com/")

'''driver.implicitly_wait(5)

search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("Selenium")
googlesearch_button = driver.find_element(By.NAME,"btnK")
googlesearch_button.click()'''




driver.quit()