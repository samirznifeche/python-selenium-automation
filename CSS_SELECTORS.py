from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# open the url
driver.get("https://amazon.com")

# Locators For Amazon Sign In Page

## Amazon Logo
driver.find_element(By.CSS_SELECTOR, ".a-icon-logo")

## Amazon Sign In
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

## "Email" Field
driver.find_element(By.ID, "ap_email")

## "Continue" Button
driver.find_element(By.CSS_SELECTOR, "input#continue")

## "Conditions OF Use" Link
driver.find_element(By.CSS_SELECTOR, "[href*='condition']")

## "Privacy Notice" Link
driver.find_element(By.CSS_SELECTOR, "[href*='/ref=ap_signin_notification_privacy_notice']")

## "Need Help?" Link
driver.find_element(By.CSS_SELECTOR, ".a-expander-prompt")

## "Forgot Your Password?" Link
driver.find_element(By.ID, "auth-fpp-link-bottom")

## "Other Issues With Sign In" Link
driver.find_element(By.ID, "ap-other-signin-issues-link")

## "Buy For Work?"
driver.find_element(By.CSS_SELECTOR, ".a-text-bold")

## "Shop on Amazon Business" Link
driver.find_element(By.CSS_SELECTOR, "#ab-signin-ingress-link span")

## "Create your Amazon account" Button
driver.find_element(By.ID, "createAccountSubmit")


# CSS_SELECTORS Home Page practice

# By tag + id
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

## By id
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')

## By tag + class
driver.find_element(By.CSS_SELECTOR, 'input.nav-input.nav-progressive-attribute')

## By class
driver.find_element(By.CSS_SELECTOR, '.nav-input.nav-progressive-attribute')

## By tag + attribute
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon']")

## By attribute
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")

# By tag + id + class
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox.nav-input')

# By id + class
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox.nav-input')

# By tag + id + attribute
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox[placeholder='Search Amazon']")

# By id + attribute
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox[placeholder='Search Amazon']")

# By tag + class + attribute
driver.find_element(By.CSS_SELECTOR, "input.nav-input[placeholder='Search Amazon']")

# By class + attribute
driver.find_element(By.CSS_SELECTOR, ".nav-input[placeholder='Search Amazon']")

# By tag + id + class + attribute
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input[placeholder='Search Amazon']")

# By id + class + attribute
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox.nav-input[placeholder='Search Amazon']")

# By using attribute partial match
driver.find_element(By.CSS_SELECTOR, "[placeholder*='Search']")