from behave import given, when, then
from datetime import date, timedelta
from pages.leave_page import LeavePage


@given('the user navigates to the Leave module')
def step_navigate_leave(context):
    context.leave_page = LeavePage(context.driver)
    context.leave_page.navigate()
    context.leave_page.click_apply()


@given('I store the initial leave balance')
def step_store_initial_balance(context):
    context.initial_leave_balance = context.leave_page.get_leave_balance()


@when('the user selects leave type "{leave_type}"')
def step_select_leave_type(context, leave_type):
    context.leave_page.select_leave_type(leave_type)


@when('the user enters from date and to date for leave')
def step_enter_leave_dates(context):
    today = date.today()
    from_date = (today + timedelta(days=1)).strftime("%Y-%m-%d")
    to_date = (today + timedelta(days=1)).strftime("%Y-%m-%d")  # 1 day leave
    context.leave_page.enter_from_date(from_date)
    context.leave_page.enter_to_date(to_date)


@when('the user submits the leave application')
def step_submit_leave(context):
    context.leave_page.click_submit()


@then('a success toast message should appear')
def step_verify_toast(context):
    assert context.leave_page.is_success_toast_displayed()


@then('the leave balance should be reduced by 1 day')
def step_verify_balance_reduced(context):
    final_balance = context.leave_page.get_leave_balance()
    expected = context.initial_leave_balance - 1
    assert final_balance == expected, \
        f"Expected balance {expected} but got {final_balance}"
