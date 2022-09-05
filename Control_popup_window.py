from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/temp/eclipse-workspace/'
                          'SeleniumFirstProject/src/seleniumFirstProject'
                          '/chromedriver')

driver.get('https://omayo.blogspot.com/')
window_main = driver.window_handles[0]

# Open popup window
driver.find_element_by_link_text('Open a popup window').click()
time.sleep(1)

# Get handle popup window
windows_popup = driver.window_handles[1]
driver.switch_to.window(windows_popup)
time.sleep(1)

# Close popup window
driver.close()
time.sleep(1)

# Switch back to main window
driver.switch_to.window(window_main)

# Control on main window (ex: input text='Test' on "Search This Blog")
driver.find_element_by_name('q').send_keys('Test')
time.sleep(2)

# Close main window
driver.close()
