from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('/Users/temp/eclipse-workspace/'
                          'SeleniumFirstProject/src/seleniumFirstProject'
                          '/chromedriver')

driver.get("https://www.amazon.com/")

# get element: menu "All"
element = driver.find_element_by_link_text("All")

# create action chain object
action = ActionChains(driver)
time.sleep(1)

# perform the operation
action.move_to_element(element).perform()
time.sleep(1)

# set focus on "Best Sellers" and then click on it
element = driver.find_element_by_link_text('Best Sellers')
action.move_to_element(element).perform()
time.sleep(1)
action.move_to_element(element).click().perform()
time.sleep(1)

driver.close()