from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LeavePage:
    LEAVE_MENU = (By.XPATH, "//span[text()='Leave']")
    APPLY_LINK = (By.XPATH, "//a[text()='Apply']")
    LEAVE_TYPE_DROPDOWN = (By.CSS_SELECTOR, ".oxd-select-text")
    FROM_DATE_INPUT = (By.XPATH, "(//input[contains(@class,'oxd-input')])[2]")
    TO_DATE_INPUT = (By.XPATH, "(//input[contains(@class,'oxd-input')])[3]")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".oxd-toast--success")
    LEAVE_BALANCE = (By.CSS_SELECTOR, ".oxd-leave-balance-text")
    LEAVE_STATUS = (By.CSS_SELECTOR, ".oxd-chip--default")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate(self):
        self.wait.until(EC.element_to_be_clickable(self.LEAVE_MENU)).click()

    def click_apply(self):
        self.wait.until(EC.element_to_be_clickable(self.APPLY_LINK)).click()

    def select_leave_type(self, leave_type):
        self.wait.until(EC.element_to_be_clickable(self.LEAVE_TYPE_DROPDOWN)).click()
        option = (By.XPATH, f"//div[@role='option']//span[text()='{leave_type}']")
        self.wait.until(EC.element_to_be_clickable(option)).click()

    def enter_from_date(self, date):
        field = self.wait.until(EC.visibility_of_element_located(self.FROM_DATE_INPUT))
        field.clear()
        field.send_keys(date)

    def enter_to_date(self, date):
        field = self.wait.until(EC.visibility_of_element_located(self.TO_DATE_INPUT))
        field.clear()
        field.send_keys(date)

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def is_success_toast_displayed(self):
        toast = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TOAST))
        return toast.is_displayed()

    def get_leave_balance(self):
        return self.wait.until(EC.visibility_of_element_located(self.LEAVE_BALANCE)).text

    def get_leave_status(self):
        return self.wait.until(EC.visibility_of_element_located(self.LEAVE_STATUS)).text
