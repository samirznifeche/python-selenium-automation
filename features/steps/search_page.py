from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SELECT_PRODUCT = (By.CSS_SELECTOR, "div[data-test*='@web/site-top-of-funnel'] img[alt*='Tazo Organic Tea']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "div[data-test='orderPickupSection'] button[id*='addToCartButton']")
SIDE_NAV_VIEW_CART_BTN = (By.CSS_SELECTOR, "a[href='/cart']")


@when('Select the product')
def select_product(context):
    context.driver.find_element(*SELECT_PRODUCT).click()
    sleep(5)


@when('Add the product to the cart & view cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(2)
    context.driver.find_element(*SIDE_NAV_VIEW_CART_BTN).click()
    sleep(5)