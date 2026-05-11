from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    ADMIN_MENU = (By.XPATH, "//span[text()='Admin']")
    USERNAME_INPUT = (By.CSS_SELECTOR, ".oxd-form .oxd-input--active")
    USER_ROLE_DROPDOWN = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[1]")
    STATUS_DROPDOWN = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[2]")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    RESULTS_TABLE = (By.CSS_SELECTOR, ".oxd-table-body")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate(self):
        self.wait.until(EC.element_to_be_clickable(self.ADMIN_MENU)).click()

    def enter_username(self, username):
        field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        field.clear()
        field.send_keys(username)

    def select_user_role(self, role):
        self.wait.until(EC.element_to_be_clickable(self.USER_ROLE_DROPDOWN)).click()
        option = (By.XPATH, f"//div[@role='option']//span[text()='{role}']")
        self.wait.until(EC.element_to_be_clickable(option)).click()

    def select_status(self, status):
        self.wait.until(EC.element_to_be_clickable(self.STATUS_DROPDOWN)).click()
        option = (By.XPATH, f"//div[@role='option']//span[text()='{status}']")
        self.wait.until(EC.element_to_be_clickable(option)).click()

    def click_search(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    def are_results_displayed(self):
        table = self.wait.until(EC.visibility_of_element_located(self.RESULTS_TABLE))
        return table.is_displayed()
