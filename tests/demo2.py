import time
from selenium import webdriver

driver=webdriver.Ie()
driver.get('http://www.google.com')
print(driver.title)
time.sleep(10)
driver.quit()