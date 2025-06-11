from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Click "Sign In" button')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(5)


@then('Verify Sign In form opened')
def verify_sign_in(context):
    expected_text = "Sign in or create account"
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']").text
    assert expected_text in actual_text, f"Error, {expected_text} message NOT in {actual_text}"
