from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_CONTAINER_TXT = (By.CSS_SELECTOR, "div[data-test='emptyCartContainer']")

    def verify_empty_cart(self, expected_text='Your cart is empty'):
        actual_text = self.driver.find_element(*self.CART_CONTAINER_TXT).text
        assert expected_text in actual_text, f"Error, expected '{expected_text}' not in '{actual_text}'"