from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
driver.get('Http://www.youtube.com')

searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.click()
searchbox.send_keys('Python tutorials')

searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbutton.click()