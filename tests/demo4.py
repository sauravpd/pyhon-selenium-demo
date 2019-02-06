from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.google.com/')
try:
	driver.find_element_by_name('q').send_keys('automation')
	driver.quit()
except Exception as e:
	print('Exception found')