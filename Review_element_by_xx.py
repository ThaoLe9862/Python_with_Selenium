from selenium import webdriver

driver = webdriver.Chrome('/Users/temp/eclipse-workspace/'
                          'SeleniumFirstProject/src/seleniumFirstProject'
                          '/chromedriver')
driver.get('https://www.facebook.com/login/')
# email
elem_id = driver.find_element_by_id('email')
print(elem_id)
# password
elem_name = driver.find_element_by_name('pass')
print(elem_name)
# forget account
elem_class = driver.find_element_by_class_name('_97w4')
print(elem_class)

elem_xpath = driver.find_element_by_xpath("//form[@id='login_form']")
print(elem_xpath)

driver.close()