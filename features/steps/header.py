from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


CART_ICON_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
ACCOUNT_BTN = (By.ID, "account-sign-in")
SEARCH_FIELD = (By.ID, "search")
SEARCH_ICON_BTN = (By.CSS_SELECTOR, "button[data-test*='@web/Search/SearchButton']")
SIDE_NAV_SIGN_IN_BTN = (By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')


@then('Click "Account" button')
def click_account(context):
    context.driver.wait.until(EC.element_to_be_clickable(ACCOUNT_BTN)).click()


@when('Search for {product}')
def search_product(context, product):
    #context.driver.wait.until(EC.presence_of_element_located(SEARCH_FIELD)).send_keys(product)
    #context.driver.wait.until(EC.element_to_be_clickable(SEARCH_ICON_BTN)).click()
    context.app.header.search_product()
    sleep(10)


@then('Click "Sign In" button')
def click_sign_in(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIDE_NAV_SIGN_IN_BTN)).click()


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(2)
    context.driver.execute_script("window.scrollBy(0,1000)", "")
    # sleep(2)

    # If you ever need to scroll up, use negative numbers: context.driver.execute_script("window.scrollBy(0, -2000)", "")

    products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in products[:8]:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)


@when('Open Cart page')
def open_cart(context):
    context.app.header.open_cart()