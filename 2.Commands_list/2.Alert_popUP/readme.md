# Alert & Popup Window Handling:
* What is Alert in Selenium? 
  *     In Selenium, alerts are typically used to notify the user of some important information or to request 
        permission to perform a particular action. Alerts can be of different types and can be triggered by various 
        events, such as clicking a button, submitting a form, or navigating to a new page.
  * When an alert is triggered, it opens up as a small pop-up window within the browser. Depending on the type 
    of alert, it may contain a message or prompt the user to input some data.

To handle alerts in Selenium, you can use the Alert interface provided by the webdriver library. 
This interface allows you to perform various actions on alerts, such as accepting or dismissing them, 
retrieving the text displayed in the alert message, or entering data into the prompt.


# Types of Alerts in Selenium
* 1) Simple Alert 
   * A simple alert is a basic message box that displays a message to the user. 
     It typically contains a single "OK" button that the user can click to dismiss the alert. 
     Simple alerts are commonly used to notify the user of some important information. 
     The simple alert class in Selenium displays some information or warning on the screen.
  
* 2) Confirmation Alert 
    * A confirmation alert is similar to a simple alert, but it contains two buttons:
     "OK" and "Cancel". It is typically used to confirm an action before it is performed. If the user clicks 
     "OK", the action is executed, otherwise it is cancelled.This confirmation alert asks permission to do 
     some type of operation.
  

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver import ActionChains
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.alert import Alert

# Create a webdriver object and open the web page
    driver = webdriver.Chrome(service=Service("C:\\drivers\\chrom.exe.exe"))
    url = "https://demo.guru99.com/test/delete_customer.php"
    driver.get(url)
    # Find the element to perform actions on
    Customer_ID = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/input')
    Customer_ID.send_keys("1234")
    alert_btn = driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr[3]/td[2]/input[1]')
    alert_btn.click()
    alert = Alert(driver)
    alert_text = alert.text
    print(alert_text)
    alert.dismiss()
    time.sleep(5)

* 3) Prompt Alert
  * A prompt alert is a type of alert that prompts the user to enter some data, such as a username or password. 
    It typically contains an input field where the user can enter the required data, as well as "OK" and "Cancel" 
    buttons. 

    If the user clicks "OK", the entered data is submitted, otherwise it is cancelled. Prompt alerts are commonly 
    used in login forms and other types of forms where user input is required. This Prompt Alert asks some input 
    from the user and Selenium webdriver can enter the text using sendkeys(” input…. “).

    

In this example, we first navigate to a page that triggers an alert box when a button is clicked. We then locate the
button and click on it to trigger the alert box. Next, we switch to the alert window using the Alert interface and
retrieve the text displayed in the alert message using the getText() method. Finally, we close the alert box and close
the webdriver.

Note that you should only use the getText() method for alerts that display a text message. For alerts that prompt 
the user for input, you should use the send_keys() method instead. Also note that the getText() method returns 
the text as a string, so you can store it in a variable or print it to the console.




