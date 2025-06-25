from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


CONTAINER = (By.CSS_SELECTOR, ".container")


@given('Open Target Help page')
def open_help_page(context):
    context.driver.get("https://help.target.com/help")


@then('Verify Target "Container" contains multiple links')
def verify_target_container(context):
    links = context.driver.wait.until(EC.presence_of_all_elements_located(CONTAINER))
    assert len(links) > 0, f"Error: {links}"