import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://www.demoblaze.com/index.html"
    LAPTOPS_LINK = (By.LINK_TEXT, "Laptops")
    PHONES_LINK = (By.LINK_TEXT, "Phones")

    def navigate(self):
        self.driver.get(self.URL)
        return self

    def click_laptops(self):
        self.click(self.LAPTOPS_LINK)
        time.sleep(1)
        from pages.category_page import LaptopsCategoryPage
        return LaptopsCategoryPage(self.driver)

    def click_phones(self):
        self.click(self.PHONES_LINK)
        time.sleep(1)
        from pages.category_page import CategoryPage
        return CategoryPage(self.driver)
