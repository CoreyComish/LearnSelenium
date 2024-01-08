# Purpose: Learn how to navigate my own site by using links

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://coreycomish.github.io/")

edu_link = driver.find_element(by=By.LINK_TEXT, value="EDUCATION")
edu_link.click()
time.sleep(2)

exp_link = driver.find_element(by=By.LINK_TEXT, value="EXPERIENCE")
exp_link.click()
time.sleep(2)

proj_link = driver.find_element(by=By.LINK_TEXT, value="PROJECTS")
proj_link.click()
time.sleep(2)

skill_link = driver.find_element(by=By.LINK_TEXT, value="SKILLS")
skill_link.click()
time.sleep(2)

about_link = driver.find_element(by=By.LINK_TEXT, value="ABOUT")
about_link.click()
time.sleep(2)

driver.implicitly_wait(0.5)
driver.quit()