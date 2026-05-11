from behave import given, when, then
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('the user navigates to the OrangeHRM login page')
def step_navigate_to_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()


@given('the user is logged in as "{username}" with password "{password}"')
def step_user_logged_in(context, username, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    context.login_page.click_login()
    # Wait until dashboard loads
    WebDriverWait(context.driver, 10).until(EC.url_contains("dashboard"))


@when('the user enters username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)


@when('the user clicks the login button')
def step_click_login(context):
    context.login_page.click_login()


@then('the current URL should contain "dashboard"')
def step_verify_url_contains_dashboard(context):
    WebDriverWait(context.driver, 10).until(EC.url_contains("dashboard"))
    current_url = context.driver.current_url
    assert "dashboard" in current_url, f"Expected 'dashboard' in URL but got: {current_url}"


@then('an error message "{message}" should be displayed')
def step_verify_error(context, message):
    actual = context.login_page.get_error_message()
    assert message in actual, f"Expected '{message}' but got '{actual}'"
