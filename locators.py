from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# open the url
driver.get("https://amazon.com")

# Locators

## By ID
driver.find_element(By.ID, "twotabsearchtextbox")

## By XPath
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
## By XPath, any tag
driver.find_element(By.XPATH, "//*[@placeholder='Search Amazon']")
## By XPath, combination of attributes
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon' and @role='searchbox']")

## by text
driver.find_element(By.XPATH, "//a[text()='Gift Cards']")

## by partial match
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_gc')]")

## by parent => child nodes
driver.find_element(By.XPATH, "//div[@class='nav-fill']//input[@type='text']")