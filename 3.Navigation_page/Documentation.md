# Refresh Button
Pressing the Browser’s Refresh Button
To simulate pressing the browser’s refresh button to reload the page using Selenium for Python, 
call refresh() method on the Web Driver object.
Example
Initialise Chrome Web Driver object as driver.
Get the URL https://pythonexamples.org/ using web driver object.
Press the browser's refresh button using driver.refresh().
    

    from selenium import webdriver
    
    # Initialize Chrome Web Driver object
    driver = webdriver.Chrome()
    
    # Get the URL
    url = "https://pythonexamples.org/"
    driver.get(url)
    
    # Perform some actions on the page (optional)
    
    # Press the browser's refresh button
    driver.refresh()
    
    # Close the browser window
    driver.quit()




# Pressing the Browser’s Forward Button
To simulate pressing the browser’s forward button programmatically using Selenium for Python,
call forward() method on the Web Driver object.
Example
Initialise Chrome Web Driver object as driver.
Get the URL https://pythonexamples.org/ using web driver object.
Find element by link text 'OpenCV' and click on the element.
Press the browser's back button using driver.back().
Press the browser's forward button using driver.forward().

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    # Initialize Chrome Web Driver object
    driver = webdriver.Chrome()
    
    # Get the URL
    url = "https://pythonexamples.org/"
    driver.get(url)
    
    # Find element by link text 'OpenCV' and click on the element
    opencv_link = driver.find_element(By.LINK_TEXT, "OpenCV")
    opencv_link.click()
    
    # Wait for the page to load (optional)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.url_changes(url))
    
    # Press the browser's back button
    driver.back()
    
    # Press the browser's forward button
    driver.forward()
    
    # Close the browser window
    driver.quit()


# Back Button 
Pressing the Browser’s Back Button
To simulate pressing of the browser’s back button programmatically using Selenium for Python, 
call back() method on the Web Driver object.

Example
Initialise Chrome Web Driver object as driver.
Get the URL https://pythonexamples.org/ using web driver object.
Find element by link text 'OpenCV' and click on the element.
Make an implicit wait of 5 seconds.
Press the browser's back button using driver.back().


    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    # Initialize Chrome Web Driver object
    driver = webdriver.Chrome()
    
    # Get the URL
    url = "https://pythonexamples.org/"
    driver.get(url)
    
    # Find element by link text 'OpenCV' and click on the element
    opencv_link = driver.find_element(By.LINK_TEXT, "OpenCV")
    opencv_link.click()
    
    # Make an implicit wait of 5 seconds (optional)
    driver.implicitly_wait(5)
    
    # Press the browser's back button
    driver.back()
    
    # Close the browser window
    driver.quit()

