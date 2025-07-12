from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SignInPage(Page):
    SIGN_IN_TXT = (By.CSS_SELECTOR, "h1[class*='styles']")
    TC_LINK = (By.CSS_SELECTOR, "[aria-label*='terms & conditions']")
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "pass")
    LOGIN_BTN = (By.CSS_SELECTOR, "[data-testid='royal-login-button']")
    ERROR_MSG = (By.CSS_SELECTOR, "div._9ay7")

    def verify_sign_in_opened(self):
        self.wait_for_url_contains('/login')

    def open_sign_in(self):
        self.driver.get("https://my.jumia.ma/interaction/E-D_sybQB_OD9px7LECBw/fr-ma/identification")
        sleep(2)

    def click_terms_link(self):
        self.wait_for_element_click(*self.TC_LINK)

    def open_fb_page(self):
        self.driver.get("https://www.facebook.com/?locale=fr_FR")

    def enter_email(self, email):
        self.input_text(email, *self.EMAIL_FIELD)

    def enter_password(self, password):
        self.input_text(password, *self.PASSWORD_FIELD)

    def click_login_button(self):
        self.click(*self.LOGIN_BTN)

    def verify_error_msg(self):
        self.find_element(*self.ERROR_MSG)