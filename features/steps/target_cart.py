from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('open target home page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    sleep(5)

@when('target home page is opened')
def target_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()
    sleep(5)

@then('verify "Your cart is empty" message is shown')
def verify_cart_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_fontSize1']").text
    assert "Your cart is empty" in actual_text, f"Error, 'Your cart is empty' message NOT in {actual_text}"



@then('click "Account" button')
def click_account(context):
    context.driver.find_element(By.ID, "account-sign-in").click()
    sleep(5)

@then('click "Sign In" button')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(5)

@then('verify Sign In form opened')
def verify_sign_in(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
    assert "Sign in or create account" in actual_text, f"Error, 'Sign in or create account' message NOT in {actual_text}"
