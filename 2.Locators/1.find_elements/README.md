# Find Element and FindElements 
Why do you need the Find Element(s) command?
Interaction with a web page requires a user to locate the web element. by using the element's ID, name, class, 
tag name, CSS selector, or XPath expression. 


However, it's important to note that not all web elements have unique IDs, and sometimes multiple elements may 
have the same name, class, or tag name. In such cases, using CSS selectors or XPath expressions may be necessary 
to identify the desired element.


The Find Element(s) command is essential in automating web interactions because it allows the automation script to
interact with specific web elements on a page, such as filling out a form, clicking a button, or retrieving
information. Without the ability to locate web elements using 


Find Element(s), it would be difficult or impossible to interact with web pages programmatically. 
There are multiple ways to uniquely identify a web element within the web page such as 

    Find Element by Id
    Find Element by Class Name
    Find Element by CSS Selector
    Find Element by Link Text
    Find Element by Name
    Find Element by Partial Link Text
    Find Element by Tag Name
    Find Element by XPath


# By Id:
* Scenario 1: HTML page with single element by given ID 
    




* Scenario 2: HTML page with multiple elements by given ID
    In the following example, we have an HTML page with two div elements whose id="xyz".
    Even though we cannot have multiple elements with the same id, this scenario is quite possible.

If find_element() function finds more than one element by the given id, then it returns only the first element.
