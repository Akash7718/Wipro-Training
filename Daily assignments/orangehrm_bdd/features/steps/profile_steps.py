from behave import given, when, then
from pages.my_info_page import MyInfoPage


@given('navigating to the My Info section')
def step_navigate_my_info(context):
    context.my_info_page = MyInfoPage(context.driver)
    context.my_info_page.navigate()


@when('updating the nickname to "{nickname}"')
def step_update_nickname(context, nickname):
    context.my_info_page.update_nickname(nickname)


@when('clicking the save button on personal details')
def step_click_save_personal(context):
    context.my_info_page.click_save()


@then('nickname should be saved successfully')
def step_verify_nickname_saved(context):
    assert context.my_info_page.is_save_successful()


@when('uploading a profile photograph "{filename}"')
def step_upload_photo(context, filename):
    context.my_info_page.upload_photo(filename)


@then('profile photograph should be updated successfully')
def step_verify_photo_updated(context):
    assert context.my_info_page.is_save_successful()
