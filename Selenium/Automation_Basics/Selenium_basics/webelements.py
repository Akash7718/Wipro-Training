import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(1)

# TEXT INPUT
text_input = driver.find_element(By.ID,"my-text-id")
text_input.clear()
text_input.send_keys("Selenium WebDriver Demo")

# PASSWORD INPUT
password_input = driver.find_element(By.NAME,"my-password")
password_input.clear()
password_input.send_keys("secret123")

#TEXTAREA
textarea = driver.find_element(By.NAME,"my-textarea")
textarea.clear()
textarea.send_keys("This is a simple message")

# CHECKBOX
checkbox = driver.find_element(By.ID,"my-check-2")
checkbox.click()

#RADIOBUTTON
radio = driver.find_element(By.ID,"my-radio-1")
radio.click()

#DROPDOWN
dropdown = driver.find_element(By.NAME,"my-select")
dropdown.click()
option = driver.find_element(By.CSS_SELECTOR,"select[name='my-select']option[value='2']")
option.click()

#MULTI-SELECT
multi_select=driver.find_element(By.NAME,"my-datalist")
multi_select.send_keys('New York')

#FILE-UPLOAD
file_upload = driver.find_element(By.NAME,"my-file")
file_upload.send_keys("C:\\Wipro Training\\Selenium\\Automation_Basics\\Selenium_basics\\waits.py")

#RANGE-SLIDER
range_slider = driver.find_element(By.NAME,"my-range")
driver.execute_script("arguments[0].value=10;", range_slider)

#colorpicker
color_picker = driver.find_element(By.NAME,"my-colors")
color_picker.send_keys("#00ff00")

#DATE-PICKER
date_picker = driver.find_element(By.NAME,"my-date")
date_picker.send_keys("2025-12-25")

#SUBMIT BUTTON
submit_btn=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
time.sleep(20)
submit_btn.click()

time.sleep(5)
driver.quit()