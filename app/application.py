from pages.main_page import MainPage
from pages.privacy_notice_page import PrivacyNotice
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.signin_page import SigninPage
from pages.amazon_terms_and_conditions_page import TermsConditionPage

class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.signin_page = SigninPage(driver)
        self.amazon_terms_conditions_page = TermsConditionPage(driver)
        self.privacy_notice_page = PrivacyNotice(driver)