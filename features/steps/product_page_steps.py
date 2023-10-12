from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "li[id*='color_name_']")

CURRENT_COLOR = (By.CSS_SELECTOR, ".selection")


@given('Open Amazon product')
def open_amazon_product(context):
    context.driver.get('https://www.amazon.com/BULLIANT-Slide-Ratchet-Dress-Oxfords/dp/B0734YR12R')
    # sleep(2)
    # context.driver.refresh()

@then('Verify User can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Black1', 'Black2538', 'Black2826', 'Dark Brown 2486', 'Orange Brown2913']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:5]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print(current_color)
        actual_colors.append(current_color)

    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match {actual_colors}'

