from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


SEARCH_INPUT = (By.ID, 'search')
SEARCH_SUBMIT = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")


@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.wait.until(EC.presence_of_element_located(SEARCH_INPUT))
    search.clear()
    search.send_keys(search_word)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_SUBMIT)).click()


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'
