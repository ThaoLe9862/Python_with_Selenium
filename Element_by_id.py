from selenium import webdriver

driver = webdriver.Chrome('/Users/temp/eclipse-workspace/'
                          'SeleniumFirstProject/src/seleniumFirstProject'
                          '/chromedriver')

# find path of html_file.html
driver.get("file:///Users/temp/Downloads/untitled/Python_with_Selenium/html_file.html")
login_form = driver.find_element_by_id("LoginForm")

print("My login form element is: ")
print(login_form)

driver.close()