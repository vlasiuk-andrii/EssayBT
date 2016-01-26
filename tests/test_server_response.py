import requests
import unittest

class tests_for_server_response(unittest.TestCase):
    global i
    i = 0

    def setUp(self):
        print('---------------------------------')
        global i
        i += 1
        print(i)

    def tearDown(self):
        print('---------------------------------')

    def test_redirect(self):
        r = requests.head("http://essaybt.com/")
        self.assertEqual(r.status_code, 301)

        r = requests.head("http://essaybt.com/online-essay-writers/")
        self.assertEqual(r.status_code, 301)

        r = requests.head("http://essaybt.com/essay-writing-service/")
        self.assertEqual(r.status_code, 301)

        r = requests.head("http://essaybt.com/contact-us/")
        self.assertEqual(r.status_code, 301)

    def test_root(self):
        r = requests.head("https://essaybt.com/")
        self.assertEqual(r.status_code, 200)

    def test_online_essay_writers(self):
        r = requests.head("https://essaybt.com/online-essay-writers/")
        self.assertEqual(r.status_code, 200)

    def test_essay_writing_service(self):
        r = requests.head("https://essaybt.com/essay-writing-service/")
        self.assertEqual(r.status_code, 200)

    def test_contact_us(self):
        r = requests.head("https://essaybt.com/contact-us/")
        self.assertEqual(r.status_code, 200)

    def test_invalid_root(self):
        r = requests.head("https://essaybt.com//")
        self.assertEqual(r.status_code, 301)

        r = requests.head("https://essaybt.com/../")
        self.assertEqual(r.status_code, 400)

        r = requests.head("https://essaybt.com/word")
        self.assertEqual(r.status_code, 404)

        r = requests.head("https://essaybt.com/id=1")
        self.assertEqual(r.status_code, 404)

    def test_invalid_online_essay_writers(self):
        r = requests.head("https://essaybt.com/online-essay-writers//")
        self.assertEqual(r.status_code, 301)

        r = requests.head("https://essaybt.com/online-essay-writers/../")
        self.assertEqual(r.status_code, 404)

        r = requests.head("https://essaybt.com/online-essay-writers/word")
        self.assertEqual(r.status_code, 404)

        r = requests.head("https://essaybt.com/online-essay-writers/id=1")
        self.assertEqual(r.status_code, 404)

    def test_invalid_essay_writing_service(self):
        r = requests.head("https://essaybt.com/essay-writing-service//")
        self.assertEqual(r.status_code, 301)

        r = requests.head("https://essaybt.com/essay-writing-service/../")
        self.assertEqual(r.status_code, 404)

        r = requests.head("https://essaybt.com/essay-writing-service/word")
        self.assertEqual(r.status_code, 404)

        r = requests.head("https://essaybt.com/essay-writing-service/id=1")
        self.assertEqual(r.status_code, 404)

    def test_invalid_contact_us(self):
        r = requests.head("https://essaybt.com/contact-us//")
        self.assertEqual(r.status_code, 301)

        r = requests.head("https://essaybt.com/contact-us/../")
        self.assertEqual(r.status_code, 404)

        r = requests.head("https://essaybt.com/contact-us/word")
        self.assertEqual(r.status_code, 404)

        r = requests.head("https://essaybt.com/contact-us/id=1")
        self.assertEqual(r.status_code, 404)

    def test_admin(self):
        r = requests.head("https://essaybt.com/admin/")
        self.assertEqual(r.status_code, 302)

