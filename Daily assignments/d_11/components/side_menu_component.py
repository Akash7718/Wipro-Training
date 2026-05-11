from selenium.webdriver.common.by import By


class SideMenuComponent:

    def __init__(self, driver):
        self.driver = driver

        self.admin_menu = (By.XPATH, "//span[text()='Admin']")
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.leave_menu = (By.XPATH, "//span[text()='Leave']")

    def click_admin(self):
        self.driver.find_element(*self.admin_menu).click()

    def click_pim(self):
        self.driver.find_element(*self.pim_menu).click()

    def click_leave(self):
        self.driver.find_element(*self.leave_menu).click()