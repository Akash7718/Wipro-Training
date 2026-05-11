from behave import given, when, then
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@given('navigating to the OrangeHRM login page')
def step_navigate_to_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()


@given('logging in as "{username}" with password "{password}"')
def step_user_logged_in(context, username, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    context.login_page.click_login()


@when('entering username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)


@when('click the login button')
def step_click_login(context):
    context.login_page.click_login()


@then('redirecting to the dashboard page')
def step_verify_dashboard(context):
    dashboard_page = DashboardPage(context.driver)
    assert dashboard_page.is_dashboard_displayed()


@then('an error message "{message}" should be displayed')
def step_verify_error(context, message):
    actual = context.login_page.get_error_message()
    assert message in actual, f"Expected '{message}' but got '{actual}'"
