from behave import given, when, then


@given('Open Target main page')
def open_main(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main_page()