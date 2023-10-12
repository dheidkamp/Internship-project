from selenium.webdriver.common.by import By
from pages.base_page import Page


class SigninPage(Page):
    SIGNIN_TEXT = (By.CSS_SELECTOR, 'h1.a-spacing-small')
    EMAIL_INPUT = (By.ID, 'ap_email')

    def verify_signin_opened(self):
        actual_text = self.driver.find_element(*self.SIGNIN_TEXT).text

        assert actual_text == 'Sign in', f'Error, expect Sign in but got {actual_text}'
        self.driver.find_element(*self.EMAIL_INPUT)