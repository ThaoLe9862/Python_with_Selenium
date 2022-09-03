from selenium import webdriver

driver = webdriver.Chrome('/Users/temp/eclipse-workspace/'
                          'SeleniumFirstProject/src/seleniumFirstProject'
                          '/chromedriver')

# find path of html_file.html
driver.get("file:///Users/temp/Downloads/untitled/Python_with_Selenium/html_file.html")
username = driver.find_element_by_name('username')
print("My input element is: ")
print(username)

driver.close()