import time
from selenium import webdriver
# open Internet explorer
driver=webdriver.Ie()
driver.get('http://www.google.com')
#print the title
print(driver.title)

# sleep for 10 seconds
time.sleep(10)
driver.quit()
