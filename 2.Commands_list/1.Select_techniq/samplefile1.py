from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://demo.guru99.com/test/login.html")
driver.maximize_window()
time.sleep(5)

# find the elements
email_address = driver.find_element(By.ID, "email")
email_address.click()
time.sleep(3)
Password = driver.find_element(By.ID, "passwd")
Password.click()
time.sleep(3)

click_on_sign = driver.find_element(By.ID, "SubmitLogin")
click_on_sign.submit()
time.sleep(3)