from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CategoryPage(BasePage):
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".card-title a")

    def get_all_product_names(self):
        elements = self.find_all(self.PRODUCT_NAMES)
        return [el.text for el in elements]


class LaptopsCategoryPage(BasePage):
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".card-title a")

    def verify_laptop_list_presence(self):
        elements = self.find_all(self.PRODUCT_NAMES)
        assert len(elements) > 0, "No laptops found in the category"
        return self
