from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductDetailsPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "div[data-test='orderPickupSection'] [id*='addToCartButton']")


    def click_add_to_cart_btn(self):
        self.wait_for_element_click(*self.ADD_TO_CART_BTN)