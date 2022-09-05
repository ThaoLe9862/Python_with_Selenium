from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/temp/eclipse-workspace/'
                          'SeleniumFirstProject/src/seleniumFirstProject'
                          '/chromedriver')
driver.get('https://www.amazon.com/')

# Input 'iphones' in search textbox
driver.find_element_by_css_selector('#twotabsearchtextbox').send_keys('iphones')
time.sleep(1)

# Click on 'Search' button
driver.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()
time.sleep(1)

# Click on "Best Sellers"
driver.find_element_by_link_text('Best Sellers').click()
time.sleep(1)

# Click on link text "Customer Service"
driver.find_element_by_partial_link_text('Service').click()
time.sleep(1)

driver.close()

