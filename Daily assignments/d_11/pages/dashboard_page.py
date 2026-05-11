from selenium.webdriver.common.by import By


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

        self.dashboard_heading = (
            By.XPATH,
            "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6"
        )

    def get_dashboard_text(self):

        return self.driver.find_element(
            *self.dashboard_heading
        ).text