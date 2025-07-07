from pages.base_page import Page
from selenium.webdriver.common.by import By


class TermsAndConditionsPage(Page):

    def verify_tc_opened(self):
        self.wait_for_url_contains('terms-conditions')