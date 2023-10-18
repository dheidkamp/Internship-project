from pages.main_page import MainPage
from pages.privacy_notice_page import PrivacyNotice
from pages.header import Header
# from pages.search_result_page import SearchResultPage
from pages.signin_page import SigninPage
from pages.internship_registration_page import InternshipRegistrationPage
class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        # self.search_result_page = SearchResultPage(driver)
        self.signin_page = SigninPage(driver)
        self.privacy_notice_page = PrivacyNotice(driver)
        self.internship_registration_page = InternshipRegistrationPage(driver)