import time
import allure
from pages.cart_page import CartPage


@allure.feature("Checkout")
@allure.story("Exercise 4: Multi-Step Flow & Component POM")
def test_place_order_checkout(driver):
    driver.get("https://www.demoblaze.com/cart.html")
    time.sleep(1)

    cart = CartPage(driver)
    modal = cart.click_place_order()
    time.sleep(1)

    purchase_data = {
        "Name": "Akash Ghorai",
        "Country": "India",
        "City": "Kolkata",
        "Card": "1234567890987654",
        "Month": "12",
        "Year": "2026",
    }

    modal.fill_purchase_form(purchase_data).click_purchase()
    time.sleep(1)

    success_msg = modal.get_success_message()
    assert "Thank you for your purchase!" in success_msg
