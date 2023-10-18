
from pages.internship_registration_page import InternshipRegistrationPage
class Application:
    def __init__(self, driver):
        self.internship_registration_page = InternshipRegistrationPage(driver)