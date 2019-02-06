from selenium import webdriver

driver=webdriver.Chrome()
# open url
driver.get('https://www.google.com/')
try:
    # find element by name
	driver.find_element_by_name('q').send_keys('automation')
	driver.quit()
except Exception as e:
    # print exception
	print('Exception found')