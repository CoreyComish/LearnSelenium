# Purpose: Practice Selenium Automation testing by running tests on the Selenium Web Form site

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

    # Test that we can select each value in the dropdown (select) box
    def testDropDownSelect(self):
        options = ["1", "2", "3"]
        select = Select(self.driver.find_element(by=By.NAME, value="my-select"))
        for option in options:
            try:
                select.select_by_value(option)
            except selenium.common.exceptions.NoSuchElementException:
                assert False
            else:
                assert True

    # Test that the correct options are all in our dropwdown (datalist) box
    def testDropDownList(self):
        options = ["San Francisco", "New York", "Seattle", "Los Angeles", "Chicago"]
        dataList = self.driver.find_element(by=By.ID, value="my-options")
        selections = dataList.find_elements(by=By.CSS_SELECTOR, value="option")
        for ele in selections:
            assert ele.get_attribute("value") in options

    # Test that the file input field works
    def testFileInput(self):
        fileInput = self.driver.find_element(by=By.NAME, value="my-file")
        fileInput.send_keys("C:/Users/corey/Downloads/CoreyComish_Resume.pdf")
        assert fileInput.get_attribute("value").replace("\\", '/') == 'C:/fakepath/CoreyComish_Resume.pdf'

    # Test that the checked checkbox is checked and can be unchecked
    def testCheckedCheckbox(self):
        checkbox = self.driver.find_element(by=By.ID, value="my-check-1")
        assert checkbox.is_selected()
        checkbox.click()
        assert checkbox.is_selected() is False

    # Test that the default checkbox is unchecked and can be checked
    def testDefaultCheckbox(self):
        checkbox = self.driver.find_element(by=By.ID, value="my-check-2")
        assert checkbox.is_selected() is False
        checkbox.click()
        assert checkbox.is_selected()

    # Test that checking a radio button unchecks the other one
    def testRadioButtons(self):
        checkedRadioButton = self.driver.find_element(by=By.ID, value="my-radio-1")
        defaultRadioButton = self.driver.find_element(by=By.ID, value="my-radio-2")
        assert checkedRadioButton.is_selected()
        assert defaultRadioButton.is_selected() is False
        defaultRadioButton.click()
        assert checkedRadioButton.is_selected() is False
        assert defaultRadioButton.is_selected()
        checkedRadioButton.click()
        assert checkedRadioButton.is_selected()
        assert defaultRadioButton.is_selected() is False

    # Test that the submit button works
    def testSubmitButton(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value="button").click()
        message = self.driver.find_element(by=By.ID, value="message")
        assert message.text == "Received!"

    def tearDown(self):
        self.driver.close()

def main():
    unittest.main()

if __name__ == "__main__":
    main()
