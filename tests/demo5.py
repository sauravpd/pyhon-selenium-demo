from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
# open url
driver.get('https://www.google.com/')
driver.find_element_by_name('q').send_keys('automation')
driver.find_element_by_name('q').send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()