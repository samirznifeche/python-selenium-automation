from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CONTAINER = (By.CSS_SELECTOR, ".container")


@given('Open Target Help page')
def open_help_page(context):
    context.driver.get("https://help.target.com/help")
    sleep(3)


@then('Verify Target "Container" contains multiple links')
def verify_target_container(context):
    links = context.driver.find_elements(*CONTAINER)
    assert len(links) > 0, f"Error: {links}"