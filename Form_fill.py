from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome('/Users/temp/eclipse-workspace/'
                          'SeleniumFirstProject/src/seleniumFirstProject'
                          '/chromedriver')
# Open create new account page
driver.get("https://www.facebook.com/r.php?locale=en_US&display=page")
time.sleep(1)

# Fill textbox
driver.find_element_by_name('firstname').send_keys('David')
time.sleep(1)

driver.find_element_by_name('lastname').send_keys('George')
time.sleep(1)

driver.find_element_by_name('reg_email__').send_keys('David.George@gmail.com')
time.sleep(1)

# Control pop-up window
# Select birthday with 10 Jun 2005
ctrMonth = driver.find_element_by_id('month')
selMonth = Select(ctrMonth)
selMonth.select_by_index(5)
time.sleep(1)

ctrDay = driver.find_element_by_id('day')
selDay = Select(ctrDay)
selDay.select_by_value("10")
time.sleep(1)

ctrYear = driver.find_element_by_id('year')
selYear = Select(ctrYear)
selYear.select_by_visible_text('2005')
time.sleep(1)

driver.close()