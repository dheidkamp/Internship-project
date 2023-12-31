from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
ORDERS_BTN = (By.ID, 'nav-orders')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')
SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')
@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()
@when('Search for {search_word}')
def search_on_amazon(context, search_word):
    context.app.header.search_product(search_word)
    # context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    # context.driver.find_element(*SEARCH_BTN). click()

@when('Click Orders')
def click_orders(context):
    context.app.header.click_orders

@when('Click on button from Signin popup')
def click_signin_from_popup(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_BTN)).click()


@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*FOOTER_LINKS)
    # print(links)
    print(f'Total links: {len(links)}')
    assert len(links) == expected_amount, f'Expected {expected_amount} links, but got {len(links)}'


@then('Verify many links are shown in the footer')
def verify_many_links(context):
    context.driver.find_element(*FOOTER_LINKS)
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) > 1