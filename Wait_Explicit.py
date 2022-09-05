from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome('/Users/temp/eclipse-workspace/'
                          'SeleniumFirstProject/src/seleniumFirstProject'
                          '/chromedriver')
driver.get('https://seleniumpractise.blogspot.com/2016/08/how-to-use-explicit-wait-in-selenium.html')

# Click on "Click me to start timer" button
driver.find_element_by_xpath("//button[contains(text(),'Click me to start timer')]").click()
timeout = 30 # second

# Get element of "WebDriver" text that will be shown after clicking "Click me to start timer"
try:
    WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located((By.XPATH, "//p[text()='WebDriver']")))
    print("'WebDriver' is displayed.")
except TimeoutException:
    print("'WebDriver' isn't displayed")
time.sleep(1)

driver.close()
