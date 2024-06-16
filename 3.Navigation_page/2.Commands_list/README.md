# YouTub link
>>https://www.youtube.com/watch?v=gylMKXr40v0&list=PLUDwpEzHYYLsuUBvuoYTlN0KsBB5t-BDa&index=5

# Get Commands:
    In Python, the "get" commands you mentioned are part of the Selenium WebDriver API,
    which provides a way to interact with web pages through code. Here are some basic 
    details about the "get" commands in Python:

* get(url): 
  * This method is used to open a new browser window and navigate to the specified URL. 
    It's the primary command to load a web page. The url parameter should be a string 
    representing the address of the web page you want to open.

Example:

    from selenium import webdriver
    
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")

* title: 
  * This property is used to retrieve the title of the current web page.It does not take any arguments.

Example:

    current_title = driver.title
    print("Current Title:", current_title)

* page_source: 
  * This property returns the HTML source code of the current web page as a string.
   It's useful when you need to extract information directly from the HTML of the page.

Example:

    html_source = driver.page_source
    print("HTML Source Code:", html_source)

* current_url:
  * This property returns the URL of the current web page as a string. It is useful when you want to retrieve 
     the URL of the page after navigating to it.


      Example:
      python
      Copy code
      current_url = driver.current_url
      print("Current URL:", current_url)


* text: 
  * This method is used to retrieve the text content of a specific web element. To use this method, 
    you would typically locate the web element using one of the WebDriver methods such as find_element_by_xpath() 
    or find_element_by_id() and then call the text method on that element.

    
    Example:
    from selenium.webdriver.common.by import By

# Assuming the element has an ID attribute
    element = driver.find_element(By.ID, "example_id")
    element_text = element.text
    print("Element Text:", element_text)

These properties and methods are handy when you need to gather information about the current state of the web page 
or extract textual content from specific elements. As mentioned, these examples assume that you've set up your 
Selenium WebDriver environment and installed the necessary packages.

These methods and properties are part of the Selenium WebDriver API and can be used in your Python scripts 
to automate interactions with web pages. Keep in mind that you should have the appropriate 
web driver (e.g., ChromeDriver, GeckoDriver) installed and configured for these commands to work correctly.

# wait command
>>https://www.youtube.com/watch?v=DE2iuBcD8L8&list=PLUDwpEzHYYLsuUBvuoYTlN0KsBB5t-BDa&index=6