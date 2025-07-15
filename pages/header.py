from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_ICON_BTN = (By.CSS_SELECTOR, "button[data-test*='@web/Search/SearchButton']")
    CART_ICON_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    ACCOUNT_BTN = (By.ID, "account-sign-in")
    SIDE_NAV_SIGN_IN_BTN = (By.CSS_SELECTOR, "div.h-border-b button[data-test='accountNav-signIn']")

    def search_product(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON_BTN)

    def open_cart(self):
        self.click(*self.CART_ICON_BTN)
        # self.open_url('cart')

    def click_account_btn(self):
        self.wait_for_element_click(*self.ACCOUNT_BTN)

    def click_sign_in_btn(self):
        self.wait_for_element_click(*self.SIDE_NAV_SIGN_IN_BTN)