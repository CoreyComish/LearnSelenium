# Purpose: Familarize self with basics of Selenium using Python

# Import the Webdriver from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Start the session
driver = webdriver.Chrome()

# Navigate to a web page
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Get title of web page
webTitle = driver.title
print('Website Title: ', webTitle)

# Establish a wait, used to make sure element is loaded on the page
driver.implicitly_wait(0.5)

# Find an element, in this case the password text box and submit button from the example site
pw_text_box = driver.find_element(by=By.NAME, value="my-password")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# Take actions on elements, here we enter a password and click the submit button
pw_text_box.send_keys("password123")
submit_button.click()

# Request element information, in this case the message we get after hitting the submit button
message = driver.find_element(by=By.ID, value="message")
text = message.text
print("Message Received: ", text)

# Close the current tab
# driver.close()

# Close the browser window
driver.quit()