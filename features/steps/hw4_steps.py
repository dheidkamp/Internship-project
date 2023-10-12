from behave import given, when, then
from selenium.webdriver.common.by import By

BESTSELLER_LINKS = (By.CSS_SELECTOR, "a[href*='zg_bs_tab']")
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
ADDED_TO_CART_TEXT = (By.CSS_SELECTOR, '.a-size-medium-plus')

@given('Open Bestsellers page')
def open_bestsellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify there are {actual_amount} links')
def verify_bestseller_links(context, actual_amount):
    actual_amount = int(actual_amount)
    links= context.driver.find_elements(*BESTSELLER_LINKS)
    print(f'Total links: {len(links)}')
    assert len(links) == actual_amount, f'Expected {actual_amount} links, but got {len(links)}'


##Second Scenerio##
@when('Add item to cart')
def add_item_to_cart(context):
    context.driver.get('https://www.amazon.com/AmazonBasics-Professional-Journal-10-5X7-5-inches/dp/B07YLTJHH4/ref=sr_1_1_ffob_sspa?crid=UDWMDXVXMI9V&keywords=notebook&qid=1691954866&sprefix=notebook%2Caps%2C135&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1')
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@then('Verify product added to cart')
def verify_product_added_to_cart(context):

    expected_result = 'Added to Cart'
    actual_result = context.driver.find_element(*ADDED_TO_CART_TEXT).text

    assert actual_result == expected_result