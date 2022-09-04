from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/temp/eclipse-workspace/'
                          'SeleniumFirstProject/src/seleniumFirstProject'
                          '/chromedriver')
# Go to ebay.com
driver.get("https://www.ebay.com/")

# Scroll
driver.execute_script("window.scrollBy(0, 600)")
time.sleep(1)

driver.close()