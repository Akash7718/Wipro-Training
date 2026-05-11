import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyInfoPage:
    MY_INFO_MENU = (By.XPATH, "//span[text()='My Info']")
    NICKNAME_INPUT = (By.XPATH, "//label[text()='Nickname']/../..//input")
    SAVE_BUTTON = (By.XPATH, "(//button[@type='submit'])[1]")
    PHOTO_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".oxd-toast--success")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_MENU)).click()

    def update_nickname(self, nickname):
        field = self.wait.until(EC.visibility_of_element_located(self.NICKNAME_INPUT))
        field.clear()
        field.send_keys(nickname)

    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    def upload_photo(self, filename):
        filepath = os.path.abspath(filename)
        file_input = self.driver.find_element(*self.PHOTO_INPUT)
        file_input.send_keys(filepath)

    def is_save_successful(self):
        toast = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TOAST))
        return toast.is_displayed()
