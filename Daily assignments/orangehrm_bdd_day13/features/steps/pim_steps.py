from behave import given, when, then
from pages.pim_page import PIMPage


@given('the user navigates to the PIM module')
def step_navigate_pim(context):
    context.pim_page = PIMPage(context.driver)
    context.pim_page.navigate()


@when('the user clicks the Add Employee button')
def step_click_add(context):
    context.pim_page.click_add_employee()


@when('I enter "{first_name}" and "{last_name}"')
def step_enter_employee_name(context, first_name, last_name):
    context.pim_page.enter_first_name(first_name)
    context.pim_page.enter_last_name(last_name)


@when('the user clicks the save button')
def step_click_save(context):
    context.pim_page.click_save()


@then('the employee should be created successfully')
def step_verify_employee_created(context):
    assert context.pim_page.is_employee_created()
