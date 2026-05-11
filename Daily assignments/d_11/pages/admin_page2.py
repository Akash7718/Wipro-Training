from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:

    def __init__(self, driver):
        self.driver = driver

        self.admin_menu = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span")

        # Username column in table
        self.username_list = (
            By.XPATH,
            "//div[@role='row']//div[2]"
        )

    def open_admin_page(self):

        self.driver.find_element(
            *self.admin_menu
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[text()='Admin']")
            )
        )

    def is_user_present(self, expected_username):

        # Get all username elements
        users = self.driver.find_elements(
            *self.username_list
        )

        # Iterate through usernames
        for user in users:

            actual_username = user.text

            print("Found User:", actual_username)

            if actual_username == expected_username:
                return True

        return False