from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open the registration page')
def open_registration_page(context):
    context.app.internship_registration_page.open_registration()



@when('Enter some test information in the input fields')
def enter_text(context):
    context.app.internship_registration_page.enter_information_name_field()
    sleep(1)
    context.app.internship_registration_page.enter_information_company_field()
    sleep(1)
    context.app.internship_registration_page.enter_information_phone_field()
    sleep(1)
    context.app.internship_registration_page.enter_information_email_field()
    sleep(1)
    context.app.internship_registration_page.enter_information_password_field()
    sleep(1)
    context.app.internship_registration_page.select_role()
    sleep(1)
    context.app.internship_registration_page.select_position()
    sleep(1)
    context.app.internship_registration_page.select_country()
    sleep(1)
    context.app.internship_registration_page.enter_information_company_size()
    sleep(1)

# def click_registration_boxes(context):
#     context.app.internship_registration_page.select_from_dropdown("Developer")


@then('Verify the right information is present')
def verify_registration(context):
    context.app.internship_registration_page.verify_registration_text_name_field()
    context.app.internship_registration_page.verify_registration_text_company_field()
    context.app.internship_registration_page.verify_registration_text_phone_field()
    context.app.internship_registration_page.verify_registration_text_email_field()
    context.app.internship_registration_page.verify_registration_text_password_field()
    context.app.internship_registration_page.verify_registration_text_company_size()