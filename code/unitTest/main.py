# Purpose: Get comfortable using Python unittest and Selenium to automate testing
# Credit: https://www.geeksforgeeks.org/writing-tests-using-selenium-python/?ref=lbp & TechWithTim (https://www.youtube.com/@TechWithTim)

import unittest
import page
from selenium import webdriver

class PythonOrgSearch(unittest.TestCase):

    # Get's called for each test case
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.python.org/")

    """
    # This gets ran automatically, because it starts with 'test'
    def testPassExample(self):
        print("Test1")
        assert True

    def testFailExample(self):
        print("Test2")
        assert False
    
    # This method will not be ran automatically, becuase it doesn't start with 'test'
    def notATest(self):
        print("This won't print")
    """

    def testTitle(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.isTitleMatches()

    def testSearchPython(self):
        mainPage = page.MainPage(self.driver)
        mainPage.searchTextElement = "pycon"
        mainPage.clickGoButton()
        searchResultPage = page.SearchResultPage(self.driver)
        assert searchResultPage.isResultsFound()
    
    # Get's called after each test case
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()