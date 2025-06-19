from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


TARGET_CIRCLE_CELLS = (By.CSS_SELECTOR, "div.sc-acea07d2-0.sKAHH div")


@given('Open Target Circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')


@then('Verify there are at least 10 benefit cells')
def verify_benefit_cells(context):
    cells = context.driver.wait.until(EC.presence_of_all_elements_located(TARGET_CIRCLE_CELLS))
    assert len(cells) >= 10, f"Error, Target Circle page does not contain at least 10 benefit cells."