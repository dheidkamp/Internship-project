from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select


class InternshipRegistrationPage(Page):
    NAME_FIELD = (By.ID, 'Full-Name')
    Name_Input = 'FirstName'
    PHONE_FIELD = (By.ID, 'phone2')
    PHONE_INPUT = '1234567890'
    EMAIL_FIELD = (By.ID, 'Email-3')
    EMAIL_INPUT = 'tester@testytest.com'
    PASSWORD_FIELD = (By.ID, 'field')
    PASSWORD_INPUT = 'Password'
    COMPANY_WEBSITE_FIELD = (By.ID, 'Company-website')
    COMPANY_WEBSITE_INPUT = 'Company12345@testertest.com'
    ROLE_MENU_FIELD = (By.ID, 'Role')
    ROLE_DEVELOPER = (By.CSS_SELECTOR, "[value = 'Developer']")
    POSITION_MENU = (By.ID, 'Position')
    POSITION_SELLER_MANAGER = (By.ID, "[value='Position']")
    COUNTRY_MENU = (By.ID, 'country-select')
    COUNTRY_USA = (By.CSS_SELECTOR, "[value='United States of America']")
    COMPANY_SIZE = (By.ID, 'Agents-amount-2')


    def open_registration(self):
        self.driver.get('https://soft.reelly.io/sign-up')

    def enter_information_name_field (self):
        self.input_text('FirstName', *self.NAME_FIELD)

    def enter_information_phone_field(self):
        self.input_text('1234567890', *self.PHONE_FIELD)

    def enter_information_email_field(self):
        self.input_text('tester@testytest.com', *self.EMAIL_FIELD)

    def enter_information_password_field(self):
        self.input_text('Password', *self.PASSWORD_FIELD)

    def enter_company_website(self):
        self.input_text('Company12345@testertest.com', *self.COMPANY_WEBSITE_FIELD)

    def select_from_dropdown(self, dropdown_locator, option):
        dropdown = self.find_element(*dropdown_locator)
        select = Select(dropdown)
        select.select_by_visible_text(option)

    def select_role(self):
        self.select_from_dropdown(self.ROLE_MENU_FIELD, "Developer")

    def select_position(self):
        self.select_from_dropdown(self.POSITION_MENU, "Director / CEO")

    def select_country(self):
        self.select_from_dropdown(self.COUNTRY_MENU, "United States of America")

    def select_company_size(self):
        self.select_from_dropdown(self.COMPANY_SIZE, "10-25")

    def verify_registration_text_name_field(self):
        actual_name = self.find_element(*self.NAME_FIELD).get_attribute('value')
        assert actual_name == self.Name_Input, f'Expected name: {self.Name_Input}, Actual name: {actual_name}'

    def verify_registration_text_phone_field(self):
        actual_name = self.find_element(*self.PHONE_FIELD).get_attribute('value')
        assert actual_name == self.PHONE_INPUT, f'Expected name: {self.PHONE_INPUT}, Actual name: {actual_name}'

    def verify_registration_text_email_field(self):
        actual_name = self.find_element(*self.EMAIL_FIELD).get_attribute('value')
        assert actual_name == self.EMAIL_INPUT, f'Expected name: {self.EMAIL_INPUT}, Actual name: {actual_name}'

    def verify_registration_text_password_field(self):
        actual_name = self.find_element(*self.PASSWORD_FIELD).get_attribute('value')
        assert actual_name == self.PASSWORD_INPUT, f'Expected name: {self.PASSWORD_INPUT}, Actual name: {actual_name}'

    def verify_enter_company_website_field(self):
        actual_name = self.find_element(*self.COMPANY_WEBSITE_FIELD).get_attribute('value')
        assert actual_name == self.COMPANY_WEBSITE_INPUT, f'Expected name: {self.PASSWORD_INPUT}, Actual name: {actual_name}'

