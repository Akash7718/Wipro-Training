import pytest

from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    # assert "Amazon" in driver.title, 'Title for amazon is not correct'
    print("\nOpened Amazon Homepage. Title @ URL verified.")

@pytest.mark.parametrize("searchproduct",[("wireless mouse"),("shoes")])

def test_search_product(driver,searchproduct):
    homepage=HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"searching product -{searchproduct}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded(),'Search results page did not load.'
    print(f"\nSearch result page loaded successfully - {searchproduct}")

@pytest.mark.parametrize("searchproduct",[("wireless mouse"),("shoes")])

def test_find_elements_amazon(driver,searchproduct):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"searching product -{searchproduct}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded(), 'Search results page did not load.'
    print(f"\nSearch result page loaded successfully - {searchproduct}")

    productlistingpage =  ProductListingPage(driver)
    productlistingpage.first_product_title()
    val =  productlistingpage.all_products()

    assert val,"No product found on Amazon search result!"

@pytest.mark.parametrize(("searchproduct","brandname"),[("wireless mouse",'Logitech'),
                                           ("shoes","Nike")])

def test_brand_filter(driver,searchproduct,brandname):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"searching product -{searchproduct}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded(), 'Search results page did not load.'
    print(f"\nSearch result page loaded successfully - {searchproduct}")

    productlistingpage = ProductListingPage(driver)
    productlistingpage.select_brand_filter(brandname)

    assert productlistingpage.check_product_titles_for_brand_filter(brandname),'Brand filter did not apply'

