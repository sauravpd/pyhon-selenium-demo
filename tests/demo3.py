from selenium import webdriver
import re

driver = webdriver.Chrome();
driver.get('https://www.w3schools.com/')
# get the page source
doc = driver.page_source
# regular expression
emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

for email in emails:
    print(email)

driver.quit()
