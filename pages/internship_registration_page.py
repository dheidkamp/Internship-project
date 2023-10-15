from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select

class InternshipRegistrationPage(Page):
    NAME_FIELD = (By.ID, 'Full-Name')
    COMPANY_FIELD = (By.ID, 'Company-4')
    PHONE_FIELD = (By.ID, 'phone2')
    EMAIL_FIELD = (By.ID, 'Email-3')
    PASSWORD_FIELD = (By.ID, 'field')
    ROLE_MENU_FIELD = (By.ID, 'Role')
    ROLE_DEVELOPER = (By.CSS_SELECTOR, "[value = 'Developer']")
    POSITION_MENU = (By.ID, 'Position')
    POSITION_SELLER_MANAGER = (By.ID, "[value='Position']")
    COUNTRY_MENU = (By.ID, 'country-select')
    COUNTRY_USA = (By.CSS_SELECTOR, "[value='United States of America']")
    COMPANY_SIZE = (By.ID, 'Agents-amount')
    def open_registration(self):
        self.driver.get('https://soft.reelly.io/sign-up')

    def enter_information_name_field (self):
        self.input_text('FirstName', *self.NAME_FIELD)

    def enter_information_company_field (self):
        self.input_text('CompanyName', *self.COMPANY_FIELD)

    def enter_information_phone_field(self):
        self.input_text('1234567890', *self.PHONE_FIELD)

    def enter_information_email_field(self):
        self.input_text('tester@testytest.com', *self.EMAIL_FIELD)

    def enter_information_password_field(self):
        self.input_text('password', *self.PASSWORD_FIELD)

    def enter_information_company_size(self):
        self.input_text('7654', *self.COMPANY_SIZE)
    #

# def select_from_dropdown(self, option):
#     select = Select(self.driver.find_element_by_id('*self.ROLE_MENU_FIELD'))
#     select.select_by_visible_text(option)

    # def select_department(self, alias: str):
    #     drop_down = self.find_element(*self.ROLE_MENU_FIELD)
    #     select = Select(drop_down)
    #     select.select_by_visible_text(alias)
    #
    # def click_boxes(self):
    #     self.click(*self.ROLE_MENU_FIELD)
    #     self.click(*self.ROLE_DEVELOPER)
    #     self.click(*self.POSITION_MENU)
    #     self.click(*self.POSITION_SELLER_MANAGER)
    #     self.click(*self.COUNTRY_MENU)
    #     self.click(*self.COUNTRY_USA)

    def verify_registration_text_name_field(self):
        expected_text = 'FirstName'
        actual_text = self.find_element(*self.NAME_FIELD).text
        assert actual_text == expected_text, f'Expected {expected_text}, but got {actual_text}'


