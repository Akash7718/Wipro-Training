from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMPage:
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    ADD_BUTTON = (By.CSS_SELECTOR, ".orangehrm-header-container button")
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".oxd-toast--success")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate(self):
        self.wait.until(EC.element_to_be_clickable(self.PIM_MENU)).click()

    def click_add_employee(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def enter_first_name(self, first_name):
        field = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT))
        field.clear()
        field.send_keys(first_name)

    def enter_last_name(self, last_name):
        field = self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_INPUT))
        field.clear()
        field.send_keys(last_name)

    def click_save(self):
        # Explicit Wait: ensure Save button is clickable before clicking
        save_btn = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        save_btn.click()

    def is_employee_created(self):
        toast = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TOAST))
        return toast.is_displayed()
