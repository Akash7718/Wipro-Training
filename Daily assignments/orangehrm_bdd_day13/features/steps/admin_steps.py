from behave import given, when, then
from pages.admin_page import AdminPage


@given('the user navigates to the Admin module')
def step_navigate_admin(context):
    context.admin_page = AdminPage(context.driver)
    context.admin_page.navigate()


@when('I enter the following search criteria:')
def step_search_with_data_table(context):
    for row in context.table:
        field = row[0]
        value = row[1]
        if field == "Username":
            context.admin_page.enter_username(value)
        elif field == "User Role":
            context.admin_page.select_user_role(value)
        elif field == "Status":
            context.admin_page.select_status(value)


@when('the user clicks the search button')
def step_click_search(context):
    context.admin_page.click_search()


@then('the search results should display matching user records')
def step_verify_results(context):
    assert context.admin_page.are_results_displayed()
