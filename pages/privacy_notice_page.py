from pages.base_page import Page


class PrivacyNotice(Page):

    def verify_opened(self):
        self.verify_partial_url('https://www.amazon.com/gp/help/customer/display.html')
