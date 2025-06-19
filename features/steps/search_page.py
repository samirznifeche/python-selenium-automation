from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


SELECT_PRODUCT = (By.CSS_SELECTOR, "[alt*='Tazo Organic']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "div[data-test='orderPickupSection'] [id*='addToCartButton']")
AD_BANNER = (By.CSS_SELECTOR, ".heroImg")


@then('Select the product')
def select_product(context):
    context.driver.wait.until(EC.invisibility_of_element_located(AD_BANNER))
    context.driver.wait.until(EC.element_to_be_clickable(SELECT_PRODUCT)).click()
    sleep(5)


@when('Click Add to cart button')
def click_add_to_cart(context):
    context.driver.wait.until(EC.presence_of_element_located(PRODUCT_TITLE))
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN)).click()