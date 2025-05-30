from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 1. Open Target url
driver.get("https://target.com")

# 2. Click "Account" btn
driver.find_element(By.XPATH, "//span[text()='Account']").click()
sleep(5)

# 3. Click SignIn btn from side navigation
driver.find_element(By.XPATH, "//span[@aria-label='My Target Hello, Guest']").click()
sleep(5)

# 4. Verify SignIn page opened
signin_element = driver.find_element(By.XPATH, "//div[contains(@class, 'sc-4de6b25a-2')]")
if signin_element:
    print("'Sign In' Exists")
else:
    print("'Sign In' Not Exists")
driver.quit()



# Bonus "Search for a Target's store" by City, State Name

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Open Target url
driver.get("https://target.com")
sleep(5)

# Click "Cedar Rapids South" button
driver.find_element(By.ID, "web-store-id-msg-btn").click()
sleep(5)

# Enter a City "Rocklin, CA"
driver.find_element(By.ID, "zip-or-city-state").send_keys("Rocklin, CA")

# Click "Look up" button
driver.find_element(By.XPATH, "//button[contains(@class, 'h-padding-h-wide')]").click()
sleep(5)

# Click "More info" link
driver.find_element(By.XPATH, "//a[@href='/sl/rocklin/2604']").click()
sleep(5)

# Verify Rocklin info page opened
rocklin_info = driver.find_element(By.XPATH, "//h1[@data-test='@store-locator/StoreHeader/Heading']")
if rocklin_info:
    print("'Rocklin' Exists!")
else:
    print("'Rocklin' Not Exists")
driver.quit()