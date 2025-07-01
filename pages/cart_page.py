from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    cart_empty_txt = 'Your cart is empty'
    cart_individual_items_txt = 'item'
    CART_CONTAINER_TXT = (By.CSS_SELECTOR, "div[data-test='emptyCartContainer']")
    ORDER_SUMMARY_MENU = (By.CSS_SELECTOR, "[data-test*='OrderSummary']")

    def verify_empty_cart(self, expected_text='Your cart is empty'):
        actual_text = self.driver.find_element(*self.CART_CONTAINER_TXT).text
        assert expected_text in actual_text, f"Error, expected '{expected_text}' not in '{actual_text}'"

    def verify_cart_has_individual_items(self):
        self.verify_partial_text(self.cart_individual_items_txt, *self.ORDER_SUMMARY_MENU)