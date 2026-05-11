import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class ProductDetailsPage(BasePage):
    ADD_TO_CART_BUTTON = (By.LINK_TEXT, "Add to cart")
    PRODUCT_LINK = (By.LINK_TEXT, "Sony vaio i5")

    def open_product(self):
        self.click(self.PRODUCT_LINK)
        return self

    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
        # WebDriverWait for alert_is_present
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        logger.info(f"Alert accepted with text: '{alert_text}'")
        return alert_text
