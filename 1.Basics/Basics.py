from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://chat.openai.com/")

time.sleep(10)