import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_LINK = (By.ID, "cartur")
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, "button[data-target='#orderModal']")

    def navigate(self):
        self.click(self.CART_LINK)
        return self

    def click_place_order(self):
        self.click(self.PLACE_ORDER_BUTTON)
        return PurchaseModal(self.driver)


class PurchaseModal(BasePage):
    NAME_INPUT = (By.ID, "name")
    COUNTRY_INPUT = (By.ID, "country")
    CITY_INPUT = (By.ID, "city")
    CARD_INPUT = (By.ID, "card")
    MONTH_INPUT = (By.ID, "month")
    YEAR_INPUT = (By.ID, "year")
    PURCHASE_BUTTON = (By.CSS_SELECTOR, "#orderModal .btn-primary")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".sweet-alert h2")

    def fill_purchase_form(self, data_dict):
        field_map = {
            "Name": self.NAME_INPUT,
            "Country": self.COUNTRY_INPUT,
            "City": self.CITY_INPUT,
            "Card": self.CARD_INPUT,
            "Month": self.MONTH_INPUT,
            "Year": self.YEAR_INPUT,
        }
        for field_name, locator in field_map.items():
            if field_name in data_dict:
                with allure.step(f"Fill field: {field_name} = {data_dict[field_name]}"):
                    self.type_text(locator, data_dict[field_name])
        return self

    def click_purchase(self):
        self.click(self.PURCHASE_BUTTON)
        return self

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
