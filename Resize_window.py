from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/temp/eclipse-workspace/'
                          'SeleniumFirstProject/src/seleniumFirstProject'
                          '/chromedriver')
driver.get('https://www.facebook.com')

# Get current window size
size = driver.get_window_size()
print('Window size: ({}, {})'.format(size['width'], size['height']))
time.sleep(1)

# Set window size
driver.set_window_size(800, 600)
time.sleep(1)

# Set minimize window size
driver.minimize_window()
time.sleep(1)

# Set maximum window size
driver.maximize_window()
time.sleep(1)

driver.close()