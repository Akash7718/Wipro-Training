import time
import allure
from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage


@allure.feature("Cart")
@allure.story("Exercise 3: Synchronization & Alerts")
def test_add_sony_vaio_to_cart(driver):
    home = HomePage(driver)
    home.navigate().click_laptops()
    time.sleep(1)
    product_page = ProductDetailsPage(driver)
    product_page.open_product()
    time.sleep(1)
    alert_text = product_page.add_product_to_cart()
    assert "Product added" in alert_text
