from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


SIGN_IN_TXT = (By.CSS_SELECTOR, ".h-margin-t-x2 div[tabindex='-1']")


@then('Verify Sign In form opened')
def verify_sign_in(context):
    expected_text = "Sign in or create account"
    actual_text = context.driver.wait.until(EC.visibility_of_element_located(SIGN_IN_TXT)).text
    assert expected_text in actual_text, f"Error, {expected_text} message NOT in {actual_text}"
