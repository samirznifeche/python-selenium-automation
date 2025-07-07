from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_TXT = (By.CSS_SELECTOR, "h1[class*='styles']")
    TC_LINK = (By.CSS_SELECTOR, "[aria-label*='terms & conditions']")

    def verify_sign_in_opened(self):
        self.wait_for_url_contains('/login')

    def open_sign_in(self):
        self.driver.get("https://www.target.com/orders?lnk=acct_nav_my_account")

    def click_terms_link(self):
        self.wait_for_element_click(*self.TC_LINK)