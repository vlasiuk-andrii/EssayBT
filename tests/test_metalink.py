import unittest
from selenium import webdriver
import time


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

    def test_root(self):
        ''' Verify the permanency of metalink  '''

        browser = self.driver
        user = 'devess'
        password = 'uen'+''+'sm3Fso5fr'
        url = 'vk.com/'
        #browser.get("http://"+user+":"+password+"@"+url)
        browser.get("http://essaybt.com")
        browser.maximize_window()
        elem = browser.find_element_by_xpath("//head/link[@href='https://essaybt.com/xmlrpc.php']")

        browser.get("http://essaybt.com/c12321")
        elem = browser.find_element_by_xpath("//head/link[@href='https://essaybt.com/xmlrpc.php']")

    def test_online_essay_writers(self):
        ''' Verify the permanency of metalink  '''

        browser = self.driver
        user = 'devess'
        password = 'uen'+''+'sm3Fso5fr'
        url = 'vk.com/'
        #browser.get("http://"+user+":"+password+"@"+url)
        browser.get("http://essaybt.com/online-essay-writers/")
        browser.maximize_window()
        elem = browser.find_element_by_xpath("//head/link[@href='https://essaybt.com/xmlrpc.php']")

        browser.get("http://essaybt.com/online-essay-writers/accfgsc")
        elem = browser.find_element_by_xpath("//head/link[@href='https://essaybt.com/xmlrpc.php']")

    def test_essay_writing_service(self):
        ''' Verify the permanency of metalink  '''

        browser = self.driver
        user = 'devess'
        password = 'uen'+''+'sm3Fso5fr'
        url = 'vk.com/'
        #browser.get("http://"+user+":"+password+"@"+url)
        browser.get("http://essaybt.com/essay-writing-service/")
        browser.maximize_window()
        elem = browser.find_element_by_xpath("//head/link[@href='https://essaybt.com/xmlrpc.php']")

        browser.get("http://essaybt.com/essay-writing-service/ujUO:JB:BBase")
        elem = browser.find_element_by_xpath("//head/link[@href='https://essaybt.com/xmlrpc.php']")

    def test_contact_us(self):
        ''' Verify the permanency of metalink  '''

        browser = self.driver
        user = 'devess'
        password = 'uen'+''+'sm3Fso5fr'
        url = 'vk.com/'
        #browser.get("http://"+user+":"+password+"@"+url)
        browser.get("http://essaybt.com/contact-us/")
        browser.maximize_window()
        elem = browser.find_element_by_xpath("//head/link[@href='https://essaybt.com/xmlrpc.php']")

        browser.get("http://essaybt.com/contact-us/ujUO:JB:BBase")
        elem = browser.find_element_by_xpath("//head/link[@href='https://essaybt.com/xmlrpc.php']")

if __name__ == "__main__":
    unittest.main()
