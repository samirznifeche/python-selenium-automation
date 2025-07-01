from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_TXT = (By.CSS_SELECTOR, "h1[class*='styles']")

    def verify_sign_in_opened(self):
        self.wait_for_url_contains('/login')