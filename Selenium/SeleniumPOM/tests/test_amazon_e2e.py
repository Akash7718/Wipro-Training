import pytest
from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage


@pytest.mark.parametrize(("searchproduct","brandname","mensize"),[
                                           ("shoes","Nike","9")])

def test_product_odering(driver,searchproduct,brandname,mensize):
    homepage=HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"searching product -{searchproduct}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded(),'Search results page did not load.'
    print(f"\nSearch result page loaded successfully - {searchproduct}")

    productlistingpage = ProductListingPage(driver)

    productlistingpage.select_brand_filter(brandname)
    print(f"Applying Brand Filter - {brandname}")

    assert productlistingpage.check_product_titles_for_brand_filter(brandname), 'Brand filter did not apply'

    productlistingpage.select_mensize_filter(mensize)
    print(f"Applying Size Filter - {mensize}")

    assert productlistingpage.check_size_in_title(mensize), "mensize filter didi not apply"
