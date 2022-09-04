from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/temp/eclipse-workspace/'
                          'SeleniumFirstProject/src/seleniumFirstProject'
                          '/chromedriver')
# Go to ebay.com
driver.get("https://www.ebay.com/")
time.sleep(1)

# Go to facebook.com
driver.get("https://www.facebook.com/")
time.sleep(1)

# Refresh webpage
driver.refresh();
time.sleep(1)

# Back to ebay.com
driver.back()
time.sleep(1)

# Forward to facebook.com
driver.forward()
time.sleep(1)

driver.close()