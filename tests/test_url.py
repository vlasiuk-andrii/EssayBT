import unittest
from selenium import webdriver
import time
import requests
from selenium.common.exceptions import NoSuchElementException


class tests_for_selenium(unittest.TestCase):
    global i
    i = 0

    def setUp(self):
        print('---------------------------------')
        self.driver = webdriver.Firefox()
        global i
        i += 1
        print(i)

    def tearDown(self):
        self.driver.close()
        print('---------------------------------')

    def test_url(self):
       ''' Verify how server reacts to broken url '''

       browser = self.driver
       user = 'devess'
       password = 'uen'+''+'sm3Fso5fr'
       url = 'dev.essaybt.com/'
       #browser.get("http://"+user+":"+password+"@"+url)
       browser.get("http://essaybt.com")
       browser.maximize_window()
       print (browser.current_url)
       # Open page

       #browser = webdriver.get("url")
       r = requests.get("url")
       print (r.status_code)




if __name__ == "__main__":
    unittest.main()
