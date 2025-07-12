from behave import given, when, then


@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in_opened()

@given('Open sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in()

@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window_id()

@when('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.sign_in_page.click_terms_link()

@when('Switch to the newly opened window')
def switch_window(context):
    context.app.base_page.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.termas_and_conditions_page.verify_tc_opened()

@then('User can close new window and switch back to original')
def switch_back(context):
    context.app.base_page.close_window()
    context.app.base_page.switch_to_window_by_id(context.original_window)

@given('Open Facebook page')
def open_fb_page(context):
    context.app.sign_in_page.open_fb_page()

@when("Enter '{your_email}' email")
def enter_email(context, your_email):
    context.app.sign_in_page.enter_email(your_email)

@when("Enter '{your_password}' password")
def enter_password(context, your_password):
    context.app.sign_in_page.enter_password(your_password)

@when('Click Login button')
def click_login(context):
    context.app.sign_in_page.click_login_button()

@then('Verify error message is shown')
def verify_error(context):
    context.app.sign_in_page.verify_error_msg()