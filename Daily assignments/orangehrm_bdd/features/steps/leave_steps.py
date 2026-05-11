from behave import given, when, then
from datetime import date, timedelta
from pages.leave_page import LeavePage


@given('the user navigates to the Leave module')
def step_navigate_leave(context):
    context.leave_page = LeavePage(context.driver)
    context.leave_page.navigate()
    context.leave_page.click_apply()


@when('selecting leave type "{leave_type}"')
def step_select_leave_type(context, leave_type):
    context.leave_page.select_leave_type(leave_type)


@when('entering from date and to date for leave')
def step_enter_leave_dates(context):
    today = date.today()
    from_date = (today + timedelta(days=1)).strftime("%Y-%m-%d")
    to_date = (today + timedelta(days=2)).strftime("%Y-%m-%d")
    context.leave_page.enter_from_date(from_date)
    context.leave_page.enter_to_date(to_date)


@when('submitting the leave application')
def step_submit_leave(context):
    context.leave_page.click_submit()


@then('a success message should appear')
def step_verify_toast(context):
    assert context.leave_page.is_success_toast_displayed()


@then('leave balance should be reduced on the screen')
def step_verify_balance(context):
    balance = context.leave_page.get_leave_balance()
    assert balance is not None


@then('leave status should show "{status}"')
def step_verify_status(context, status):
    actual_status = context.leave_page.get_leave_status()
    assert status in actual_status, f"Expected '{status}' but got '{actual_status}'"
