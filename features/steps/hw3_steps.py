from behave import given, when, then
from selenium.webdriver.common.by import By
# @given('Open Amazon page')
# def open_amazon_page(context):
#     context.driver.get('https://www.amazon.com/')


@when('Click on Orders')
def click_on_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


# @then('Verify Sign in page opened')
# def verify_sign_in_result(context):
#     expected_result = 'Sign in'
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').text
#     assert expected_result == actual_result, f'Error, expect {expected_result} did not match {actual_result}'
#
#     assert context.driver.find_element(By.ID, 'ap_email'), 'Error, expect email input field'


###Second Scenario###
@when('Click on cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart').click()


@then('Verify Amazon cart is empty')
def amazon_cart_empty(context):
    expected_text = 'Your Amazon Cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h2").text
    assert expected_text == actual_text, f'Error, expect {expected_text} did not match {actual_text}'
