from selenium import webdriver

driver = webdriver.Chrome('/Users/temp/eclipse-workspace/'
                          'SeleniumFirstProject/src/seleniumFirstProject'
                          '/chromedriver')

# find path of html_file.html
driver.get("file:///Users/temp/Downloads/untitled/Python_with_Selenium/html_file.html")
login_form_absolute = driver.find_element_by_xpath("/html/body/form[1]")
login_form_relative = driver.find_element_by_xpath("//form[1]")
login_form_id = driver.find_element_by_xpath("//form[@id='LoginForm']")
print("My login form is: ")
print(login_form_absolute)
print(login_form_relative)
print(login_form_id)

driver.close()