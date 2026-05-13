import sys
import os
from typing import cast

from selenium.webdriver.common.devtools.v145.page import capture_screenshot

from libraries.logger import LogGen
from libraries.screensort_util import ScreenshotUtil

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from SeleniumLibrary import SeleniumLibrary

from robot.api.deco import keyword
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from robot.libraries.BuiltIn import BuiltIn


from resources.locators.signup_locators import (
    SIGNUP_LINK,
    USERNAME_TEXTBOX,
    PASSWORD_TEXTBOX,
    SIGNUP_BUTTON
)

from resources.variables.config import config

from resources.variables.testdata import (
    SIGNUP_USERNAME,
    SIGNUP_PASSWORD
)

logger  = LogGen.loggen()
class SignupPage:
    def __init__(self):
        self.selenium = cast(
            SeleniumLibrary,
            BuiltIn().get_library_instance(
                "SeleniumLibrary"
            ))

    @keyword
    def launch_demoblaze_application(self):
        self.selenium.open_browser(
            url=config.base_url,
            browser=config.browser
        )
        logger.info('Opening Browser and Launching the demo blaze Application')
        self.selenium.maximize_browser_window()
        self.selenium.set_selenium_implicit_wait(
            config.implicit_wait
        )

    @keyword
    def click_signup_link(self):
        logger.info('Clicking signup link')
        self.selenium.click_element(
            SIGNUP_LINK
        )

    @keyword
    def enter_username(self):
        logger.info('Entering username')
        self.selenium.input_text(
            USERNAME_TEXTBOX,
            SIGNUP_USERNAME
        )

    @keyword
    def enter_password(self):
        logger.info('Entering password')
        self.selenium.input_text(
            PASSWORD_TEXTBOX,
            SIGNUP_PASSWORD
        )

    @keyword
    def click_register_button(self):
        logger.info('Clicking signup button')
        self.selenium.click_button(
            SIGNUP_BUTTON
        )

    @keyword
    def verify_signup_success_alert(self):
        logger.info('Verifying success alert')
        try:
            WebDriverWait(self.selenium.driver, 10).until(  EC.alert_is_present()  )
            alert = Alert(self.selenium.driver)
            logger.info(f'Alert Text: {alert.text}')
            ScreenshotUtil.capture_screenshot(self.selenium.driver,'signup_success')
            alert.accept()
        except TimeoutException:
            logger.info('Signup success alert')
            ScreenshotUtil.capture_screenshot(self.selenium.driver, 'signup_success_timeout')
            raise AssertionError(  "Signup alert did not appear" )