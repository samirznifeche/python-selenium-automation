from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")


@then('Select the product')
def select_product(context):
    context.app.search_results_page.select_product()
    sleep(5)

@then('Verify search worked for tea')
def verify_search_worked(context):
    context.app.search_results_page.verify_search_results()