from selenium import webdriver
import unittest

class GoogleSearchTest(unittest.TestCase):
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def googleSearchTest(self):
        self.driver.get('http://www.google.com')
        self.driver.find_element_by_class_name('q').send_keys('test automation')

    def tearDown(self):
        self.driver.quit()




