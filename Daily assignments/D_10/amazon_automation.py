import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation_and_title():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.amazon.in')

    #verifying that title contains Amazon
    title=driver.title
    assert "Amazon" in title,"Title verification Failed"
    print ("Test verification Passed")

    #Clicking on mobile category
    mobiles = driver.find_element(By.CSS_SELECTOR,"#nav-xshop > ul > li:nth-child(5) > div > a")
    mobiles.click()
    time.sleep(5)
    driver.back() #back to home page
    time.sleep(3)
    driver.quit()

def test_search_bar():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.amazon.in')
    time.sleep(5)

    #search bar using ID
    search_bar=driver.find_element(By.ID,"twotabsearchtextbox")
    search_bar.send_keys("Wireless Headphones")

    #search button using XPATH
    search_button = driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button']")
    search_button.click()

    #verifying
    page_text=driver.page_source
    assert "Wireless Headphones" in page_text,"Search result not found"

    driver.quit()

def test_implicit_explicit_waits():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.amazon.in')
    time.sleep(5)

    #search laptop
    search_box=driver.find_element(By.ID,"twotabsearchtextbox")
    search_box.send_keys("Dell Laptop")

    search_button=driver.find_element(By.ID,"nav-search-submit-button")
    search_button.click()

    first_product=WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.CLASS_NAME,"a-truncate-cut")))
    first_product.click()
    time.sleep(3)
    driver.quit()

def test_footer_links():

    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.amazon.in")
    time.sleep(2)

    # Clicking About Us using CSS Selector
    about_us = driver.find_element(By.CSS_SELECTOR, "a[href*='aboutamazon']")
    about_us.click()
    time.sleep(3)

    # Find element using link text
    element = driver.find_element(By.NAME, "featureFlags")
    print("Text Found :")
    print(element.get_attribute("content"))
    driver.quit()


# Exercise 5
def test_filters_and_sync():

    driver = webdriver.Edge()

    # Implicit wait
    driver.implicitly_wait(10)

    driver.maximize_window()
    driver.get("https://www.amazon.in")

    # Search Smart Watches
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("Smart Watches")

    driver.find_element(By.ID, "nav-search-submit-button").click()

    # Wait for filters
    brand_filter = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='p_123/42717']/span/a")
        )
    )

    # Click Samsung brand
    brand_filter.click()

    # Wait for updated products
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "s-image")
        )
    )

    # Count products
    products = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
    print("Number of products displayed :", len(products))

    time.sleep(3)
    driver.quit()
