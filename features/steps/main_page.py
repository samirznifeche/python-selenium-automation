from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_ICON_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
ACCOUNT_BTN = (By.CSS_SELECTOR, "a#account-sign-in span")
SEARCH_FIELD = (By.ID, "search")
SEARCH_ICON_BTN = (By.CSS_SELECTOR, "button[data-test*='@web/Search/SearchButton']")


@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    sleep(5)


@when('Target home page is opened')
def target_cart(context):
    context.driver.find_element(*CART_ICON_BTN).click()
    sleep(5)


@then('Click "Account" button')
def click_account(context):
    context.driver.find_element(*ACCOUNT_BTN).click()
    sleep(5)


@then('Search for a {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_ICON_BTN).click()
    sleep(15)
