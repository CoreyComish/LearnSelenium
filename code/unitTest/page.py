from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "q"

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    searchTextElement = SearchTextElement()

    def isTitleMatches(self):
        return "Python" in self.driver.title
    
    def clickGoButton(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultPage(BasePage):

    def isResultsFound(self):
        return "No results found." not in self.driver.page_source