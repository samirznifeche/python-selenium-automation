from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


CART_ICON_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
ACCOUNT_BTN = (By.ID, "account-sign-in")
SIDE_NAV_SIGN_IN_BTN = (By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")
SEARCH_FIELD = (By.ID, "search")
SEARCH_ICON_BTN = (By.CSS_SELECTOR, "button[data-test*='@web/Search/SearchButton']")


@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Open Cart page')
def open_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(CART_ICON_BTN)).click()


@then('Click "Account" button')
def click_account(context):
    context.driver.wait.until(EC.element_to_be_clickable(ACCOUNT_BTN)).click()


@then('Click "Sign In" button')
def click_sign_in(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIDE_NAV_SIGN_IN_BTN)).click()


@then('Search for {product}')
def search_product(context, product):
    context.driver.wait.until(EC.presence_of_element_located(SEARCH_FIELD)).send_keys(product)
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_ICON_BTN)).click()
    sleep(10)