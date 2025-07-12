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

@given('Open Help page for Returns')
def open_help_returns_page(context):
    context.app.help_page.open_help_returns_page()

@when('Select Help {value} topic')
def select_help_circle_topic(context, value):
    context.app.help_page.select_help_circle_topic(value)

@then('Verify Help {expected_header_text} page opened')
def verify_help_circle_page_opened(context, expected_header_text):
    context.app.help_page.verify_help_topic_page_opened(expected_header_text)