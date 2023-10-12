from behave import *


@given('Store original windows')
def store_original_window(context):
    context.original_window = context.app.amazon_terms_conditions_page.store_original_window()


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.app.amazon_terms_conditions_page.click_privacy_link()


@when('Switch to the newly opened window')
def switch_window(context):
    context.app.amazon_terms_conditions_page.switch_to_new_window()
