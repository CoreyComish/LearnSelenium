# Purpose: Practice performing actions by automating Cookie Clicker

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

# Click the English Language button
eng_link = driver.find_element(by=By.ID, value="langSelect-EN")
eng_link.click()
time.sleep(5)

# Get the clickable cookie and the cookie count
cookie = driver.find_element(by=By.ID, value="bigCookie")
cookie_count = driver.find_element(by=By.ID, value="cookies")

# Get the upgrades on the right side of the screen
upgrades = [driver.find_element(by=By.ID, value="productPrice" + str(i)) for i in range(19, -1, -1)]

# Click the cookie (randomly), if we can get an upgrade, click it!
# Note that this breaks at some point, since upgrades eventually stop being listed as numbers (ie. '1.4 million')
while True:
    cookie.click()
    time.sleep(random.random())
    count = int(cookie_count.text.split(" ")[0].replace(",", ""))
    for upgrade in upgrades:
        try:
            val = int(upgrade.text.replace(",", ""))
        except:
            pass
        else:
            if val <= count:
                upgradeActions = ActionChains(driver)
                upgradeActions.move_to_element(upgrade)
                upgradeActions.click()
                upgradeActions.perform()