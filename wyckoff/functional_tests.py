from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/Users/Oliver/Downloads/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_enter_pair_and_retrieve_ohlc(self):
        # Otis is interested in the Wyckoff trading method and found
        # an online app to help evaluate forex using Wykoffian principles
        browser.get('http://localhost:8000')

        # He notices Wyckoff in the title and header of the page
        self.assertIn('Wyckoff', self.browser.title)
        self.fail('Finish the test!')

        # He can enter a forex pair (EUR/USD) into a text box
        # the open, high, low and close of the previous day are diplayed on the page

        # Otis wonders what more this awesome application will do

if __name__ == '__main__':
    unittest.main()

