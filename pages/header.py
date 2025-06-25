from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_ICON_BTN = (By.CSS_SELECTOR, "button[data-test*='@web/Search/SearchButton']")
    CART_ICON_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")

    def search_product(self):
        self.input_text('tea', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON_BTN)

    def open_cart(self):
        self.click(*self.CART_ICON_BTN)