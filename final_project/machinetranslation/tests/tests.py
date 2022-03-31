import unittest
from translator import *

class MyTestCase1(unittest.TestCase):
    def test_something(self):
        self.assertEqual(english_to_french(" "), " ")  # test for null

class MyTestCase2(unittest.TestCase):
    def test_something(self):
        self.assertEqual(french_to_english(" "), " ")  # test for null

class MyTestCase3(unittest.TestCase):
    def test_something(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")  # test for 'Hello'/'Bonjour'

class MyTestCase4(unittest.TestCase):
    def test_something(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")  # test for 'Hello'/'Bonjour'

if __name__ == '__main__':
    unittest.main()

