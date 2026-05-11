from selenium.webdriver.common.by import By

class PersonalDetailsPage:

    def __init__(self, driver):
        self.driver = driver

        self.personal_details_heading = (
            By.XPATH,
            "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]"
        )

    def is_personal_details_displayed(self):
        return self.driver.find_element(
            *self.personal_details_heading
        ).is_displayed()