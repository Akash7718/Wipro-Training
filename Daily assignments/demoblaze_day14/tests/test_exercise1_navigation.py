import allure
from pages.home_page import HomePage


@allure.feature("Navigation")
@allure.story("Exercise 1: BasePage & Chaining")
def test_navigate_to_laptops(driver):
    home = HomePage(driver)
    home.navigate().click_laptops().verify_laptop_list_presence()
