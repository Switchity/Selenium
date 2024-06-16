# Step 1:
We need to import this package to create objects of Web Elements

    import time
    from selenium import webdriver
    from selenium.webdriver import ActionChains
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By


# Step 2:
We need to call the findElement() method available on the WebDriver class and get an object of 
WebElement.

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service("C:\\drivers\\chrom.exe.exe"))

# Provided the URL
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    time.sleep(3)





