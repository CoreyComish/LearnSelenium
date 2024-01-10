# Purpose: Practice Selenium Automation testing by running tests on the Selenium Web Form site

from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions
import unittest

TITLE = "Web form"
TEST_TEXT = "123 qwe ASD !?#"

class webTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        self.driver.implicitly_wait(5)

    # Test if the websites Title is correct
    def testTitle(self):
        assert self.driver.title == TITLE

    # Test if a "valid" login works
    def testValidLogin(self):
        self.driver.find_element(by=By.ID, value="my-text-id").send_keys("username")
        self.driver.find_element(by=By.NAME, value="my-password").send_keys("password123")
        self.driver.find_element(by=By.CSS_SELECTOR, value="button").click()
        message = self.driver.find_element(by=By.ID, value="message")
        assert message.text == "Received!"

    # Test if a text area allows different types of text
    def testTextArea(self):
        textArea = self.driver.find_element(by=By.NAME, value="my-textarea")
        textArea.send_keys(TEST_TEXT)
        assert textArea.get_attribute("value") == TEST_TEXT

    # Test if disabled input is truly disabled
    def testDisabledInput(self):
        disabledInput = self.driver.find_element(by=By.NAME, value="my-disabled")
        try:
            disabledInput.send_keys(TEST_TEXT)
        except selenium.common.exceptions.ElementNotInteractableException:
            assert True
        else:
            assert False

    # Test if read only input is truly read only
    def testReadOnlyInput(self):
        readOnlyInput = self.driver.find_element(by=By.NAME, value="my-readonly")
        readOnlyInput.send_keys(TEST_TEXT)
        assert readOnlyInput.get_attribute("value") == "Readonly input"

    # Test that the 'Return to index' link works correctly
    def testReturnToIndex(self):
        link = self.driver.find_element(by=By.LINK_TEXT, value="Return to index")
        link.click()
        assert self.driver.current_url == "https://www.selenium.dev/selenium/web/index.html"

    def tearDown(self):
        self.driver.close()

def main():
    unittest.main()

if __name__ == "__main__":
    main()
