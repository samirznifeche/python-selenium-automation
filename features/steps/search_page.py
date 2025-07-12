from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")


@then('Select the product')
def select_product(context):
    context.app.search_results_page.select_product()
    sleep(5)

@when('Hover favorites icon')
def hover_fav_icon(context):
    context.app.search_results_page.hover_fav_icon()

@then('Verify search worked for tea')
def verify_search(context):
    context.app.search_results_page.verify_search_results()

@then('Favorites tooltip is shown')
def verify_fav_tt_shown(context):
    context.app.search_results_page.verify_fav_tt_shown()