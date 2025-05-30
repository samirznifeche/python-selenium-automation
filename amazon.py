from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# Amazon Logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Email field
driver.find_element(By.ID, "ap_email")

# Continue button
driver.find_element(By.ID, "continue")

# Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# Privacy notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link
driver.find_element(By.ID, "auth-fpp-link-bottom")

# Other issues with SignIn link
driver.find_element(By.ID, "ap-other-signin-issues-link")

# Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit")
print("Test passed")
driver.quit()