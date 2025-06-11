from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_CONTAINER_TXT = (By.CSS_SELECTOR, "div[data-test='emptyCartContainer']")
ORDER_SUMMARY_TXT = (By.CSS_SELECTOR, "div[class*='h-margin-b-default'] button[aria-label*='Order Summary']")


@then('Verify "Your cart is empty" message is shown')
def verify_cart_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(*CART_CONTAINER_TXT).text
    assert expected_text in actual_text, f"Error, '{expected_text}' message NOT in {actual_text}"


@then("Verify cart has individual items")
def verify_cart_has_individual_items(context):
    actual_text = context.driver.find_element(*ORDER_SUMMARY_TXT).text
    assert "1 item" in actual_text, f"Error, '1 item' message NOT in {actual_text}"