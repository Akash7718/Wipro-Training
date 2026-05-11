import allure
from pages.home_page import HomePage


@allure.feature("Product Search")
@allure.story("Exercise 2: List Elements & Dynamic Data")
def test_phones_category_contains_samsung(driver):
    home = HomePage(driver)
    category_page = home.navigate().click_phones()
    product_names = category_page.get_all_product_names()
    assert "Samsung galaxy s6" in product_names, \
        f"'Samsung galaxy s6' not found in {product_names}"
