from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Load Google Website
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# Use the search bar to search for "test"
search = driver.find_element(by=By.NAME, value="q")
search.send_keys("test")
search.send_keys(Keys.RETURN)

# Prints out the search results on the first page
content = driver.find_element(by=By.ID, value="rso")
#print(content.text)

# Prints out the featured snippet from the search result
feat_snip = driver.find_element(by=By.CLASS_NAME, value="xpdopen")
print(feat_snip.text)

# Clicks on the images link
img_link = driver.find_element(by=By.LINK_TEXT, value="Images")
img_link.click()

driver.implicitly_wait(5)
driver.quit()