import time
from pydoc import locate

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.relative_locator import locate_with

driver =  webdriver.Edge(service = Service("../resources/msedgedriver.exe"))

# driver.get("https://www.google.com/")

#ID
# search_input = driver.find_element(By.ID,"APjFqb")
# search_input.send_keys("selenium")
# time.sleep(3)
# search_input.clear()

#Name
# search_input = driver.find_element(By.NAME,"q")
# search_input.send_keys("locators")
# time.sleep(3)

#Name
# googlesearch_button = driver.find_element(By.NAME,"btnK")
# googlesearch_button.click()
# time.sleep(30)

#classname
# imfl_button = driver.find_element(By.CLASS_NAME,"RNmpXc")
# imfl_button.click()
# time.sleep(3)

#Tagname
# href_elements = driver.find_elements(By.TAG_NAME,"a")
# for elmt in href_elements:
#     print(f'{elmt.text}-{elmt.get_attribute("href")}')

#linktext
# images_link = driver.find_element(By.LINK_TEXT,"Images")
# images_link.click()
# time.sleep(10)

#Partial LT
# images_link = driver.find_element(By.PARTIAL_LINK_TEXT,"ma")
# images_link.click()
# time.sleep(10)

#CSS Selectors
# search_input = driver.find_element(By.CSS_SELECTOR,'div > textarea')
# search_input.send_keys('selenium')
# time.sleep(5)

#xpath
# settings_test = driver.find_element(By.XPATH,'  ')
# print(settings_test.text)
# time.sleep(5)


# driver.get("https://the-internet.herokuapp.com/tables")
# time.sleep(5)
#AND & OR expression
# and_example = driver.find_element(By.XPATH,"//td[text()='Tim' and @class = 'first_name']")
# print(f"AND Example -> Found with both conditions :{and_example.text}")
#
# or_example = driver.find_element(By.XPATH,"//td[text()='Tim' or text() = 'Frank']")
# print(f"AND Example -> Found with both conditions :{and_example.text}")


'''#child - select all 'td' elements that are direct children of a row
rows = driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr/td")
print(f"Child Example -> Found{len(rows)}columns in the first table.")

#Parent - get the parent row of a particular cell
email_cell = driver.find_element(By.XPATH,"//table[@id='table1]//td[text()='jdoe@hotmail.com']")
parent_row = driver.find_element(By.XPATH,"//table[@id='table1]//td[text()='jdoe@hotmail.com']/parent::tr")
print(f"Parent Example-> Email'{email_cell.text}'belongs to row with first name: "
      f"{parent_row.find_element(By.XPATH,'./td[2]').text}")

'''
#Ancestor
'''ancestor_table = driver.find_element(By.XPATH,"//td[text()='jsmith@gmail.com']/ancestor::table")
print(f"Ancestor Example -> Table ID:{ancestor_table.get_attribute('id')}")

#descendant
descendant = driver.find_elements(By.XPATH,"//table[@id='table1']/descendant::td")
print(f"Descendant Examle -> Found {len(descendant)} descendant cells")
'''

driver.get("https://www.saucedemo.com/")
time.sleep(5)

username_field = driver.find_element(By.ID,"user-name")
password_field = driver.find_element(By.ID,"password")
login_button = driver.find_element(By.ID,"login-button")
#above
elmt_above_password = driver.find_element(
    locate_with(By.TAG_NAME,"input").above(password_field)
)
print(f"Above Example -> Text above password:{elmt_above_password.get_attribute('placeholder')}")
elmt_above_password.send_keys('standard_user')
time.sleep(5)
#below
field_below_username = driver.find_element(
    locate_with(By.TAG_NAME,"input").below(username_field)
)
print(f"Below Example -> Placeholder below username:{field_below_username.get_attribute('placeholder')}")
field_below_username.send_keys('secret_sauce')
time.sleep(5)
login_button.click()
time.sleep(2)

#toRightof
twitter_icon = driver.find_element(By.LINK_TEXT,"Twitter")
facebook_icon = driver.find_element(locate_with(By.TAG_NAME,"a").to_right_of(twitter_icon))
print(f"toRightof Example -> Element to the Right of Twitter icon has href:{facebook_icon.get_attribute('href')}")

#toleftof
left_icon = driver.find_element(locate_with(By.TAG_NAME,"a").to_left_of(facebook_icon))
print(f"toLeftof Example -> Element to the Left of Facebook icon has href:{left_icon.get_attribute('href')}")

#near
near_twitter = driver.find_element(locate_with(By.TAG_NAME,"a").near(twitter_icon))
for element in near_twitter:
    print(f"Near Example -> Element near twitter icon has href:{element.get_attribute('href')}")


time.sleep(5)
driver.quit()