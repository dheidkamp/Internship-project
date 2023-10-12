from selenium.webdriver.common.by import By


from pages.base_page import Page


class TermsConditionPage(Page):
    PRIVACY_NOTICE_LOCATOR = (By.CSS_SELECTOR, 'a.help-display-cond[href*="https://www.amazon.com/privacy"]')

    def store_original_window(self):
        return self.get_current_window()

    def click_privacy_link(self):
        self.click(*self.PRIVACY_NOTICE_LOCATOR)
