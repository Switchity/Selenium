# What is a CSS Selector?
CSS (Cascading Style Sheets) is a styling language used to describe how elements on a web page should be displayed. 

CSS Selectors are a way to select specific elements on a web page based on their attributes such as ID, class, tag, 
or other attributes.They are string representations of HTML tags, attributes, Id and Class.  As such they are 
patterns that match against elements in a tree and are one of several technologies that can be used to select
nodes in an XML document.

# Simple
* By ID:
  * An element’s id in XPATH is defined using: “[@id='example']” and in CSS using: “#” - IDs must be unique within the DOM.


    Examples:
    XPath: //div[@id='example']
    CSS:		div #example

Element Type
The previous example showed //div in the xpath. That is the element type, which could be input for a text box or 
button, img for an image, or "a" for a link. 

        Xpath: //input or
        Css: =input

* Direct Child 
  * HTML pages are structured like XML, with children nested inside of parents. If you can locate, for example, 
    the first link within a div, you can construct a string to reach it. A direct child in XPATH is defined by the
    use of a “/“, while on CSS, it’s defined using “>”
  

      Examples:
      XPath: //div/a
      CSS: div > a



* Child or Sub-Child 
  * Writing nested divs can get tiring - and result in code that is brittle. Sometimes you expect the code to 
   change, or want to skip layers. If an element could be inside another or one of its children, it’s defined in 
   XPATH using “//” and in CSS just by a whitespace.
  

      Examples:
      XPath: 	//div//a
      CSS:	 	div#a

Syntax
    css=tag#id
Css = tag(the HTML tag of the element being accessed)#( always be present when using css)id(the element being accessed)


tag  (The HTML tag of the element being accessed )# ( the hash sign)id (the ID of the element being accessed)
Step 1. 
Url =  https://demo.guru99.com/test/facebook.html


“css=input#email”




Class
For classes, things are pretty similar in XPATH: “[@class='example']” while in CSS it’s just “.”
Examples:
XPath: 	//div[@class='example']
CSS: 		div.example

CSS Selector in Selenium using an HTML tag and a class name is similar to using a tag and ID, but in this case, a dot (.) is used instead of a hash sign.


Syntax  css=tag.classvalue
Step 1.
Url = http://demo.guru99.com/test/facebook.html


























    Class =  "inputtext"
  	  input.inputtext














































II: Advanced
Next Sibling
This is useful for navigating lists of elements, such as forms or ul items. The next sibling will tell selenium to find the next adjacent element on the page that’s inside the same parent. Let’s show an example using a form to select the field after the username.

XPATH:	 //input[@id='username']/following-sibling:input[1]
CSS:		 #username + input


Attribute Values
If you don’t care about the ordering of child elements, you can use an attribute selector in selenium to choose elements based on any attribute value. A good example would be choosing the ‘username’ element of the form above without adding a class.

We can easily select the username element without adding a class or an id to the element.

XPATH: 	//input[@name='username']
CSS:		 input[name='username']

We can even chain filters to be more specific with our selectors.

XPATH: 	//input[@name='login'and @type='submit']
CSS: 		input[name='login'][type='submit']

Here Selenium will act on the input field with name="login" and type="submit"





Example: 
This strategy uses the HTML tag and a specific attribute of the element to be accessed.
Syntax  css=tag[attribute=value]





tag = the HTML tag of the element being accessed


[ and ] = square brackets within which a specific attribute and its corresponding value will be placed


attribute = the attribute to be used. It is advisable to use an attribute that is unique to the element such as a name or ID.
value = the corresponding value of the chosen attribute.




Step 1. 


Url =  http://demo.guru99.com/test/newtours/register.php













Xpath ==  //input[@name="firstName" ]



Css Selector === input[name="firstName" ]





Xpath = //input[@name="firstName" and @ size="20" ]

Css selector = input[name="firstName" and size="20" ]



Choosing a Specific Match
CSS selectors in Selenium allow us to navigate lists with more finesse than the above methods. 

If we have a ul and we want to select its fourth li element without regard to any other elements, we should use nth-child or nth-of-type. Nth-child is a pseudo-class. In straight CSS, that allows you to override behavior of certain elements; we can also use it to select those elements.

<ul id = "recordlist">
<li>Cat</li>
<li>Dog</li>
<li>Car</li>
<li>Goat</li>
</ul>

If we want to select the fourth li element (Goat) in this list, we can use the nth-of-type, which will find the fourth li in the list. Notice the two colons, a recent change to how 



Xpath ==//table[@border="2"]//child::tr[1]

Css selector ===table[border="2"]child::tr[1]










CSS identifies pseudo-classes.

CSS: #recordlist li::nth-of-type(4)



On the other hand, if we want to get the fourth element only if it is a li element, we can use a filtered nth-child which will select (Car) in this case.

CSS: #recordlist li::nth-child(4)

Note, if you don’t specify a child type for nth-child it will allow you to select the fourth child without regard to type. This may be useful in testing css layout in selenium.

CSS: #recordlist *::nth-child(4)

In XPATH this would be similar to using [4].





Substring Matches
CSS in Selenium has an interesting feature of allowing partial string matches using ^=, $=, or *=. I’ll define them, then show an example of each:
^= Match a prefix
CSS: a[id^='id_prefix_']

A link with an “id” that starts with the text “id_prefix_”
$= Match a suffix
CSS: a[id$='_id_sufix']

A link with an “id” that ends with the text “_id_sufix”
*= Match a substring
CSS: a[id*='id_pattern']

A link with an “id” that contains the text “id_pattern”

Syntax
css=tag.classvalue[attribute=value]


Step 1. 
Url = http://demo.guru99.com/test/facebook.html



Tage.classvalue[class =classvalue]


>> input.inputtext[calss=inputtext]


As you may have noticed, HTML labels are seldom given id, name, or class attributes. So, how do we access them? The answer is through the use of their inner texts. Inner texts are the actual string patterns that the HTML label shows on the page.
Syntax  css=tag:contains("inner text")


tag = the HTML tag of the element being accessed
inner text = the inner text of the element


Step 1. Navigate to Mercury Tourshomepage


Url =  http://demo.guru99.com/test/newtours/



font:contains(“password”)


//font:contains("password")

These are just a few examples of how to use CSS selectors in Selenium. By using CSS selectors effectively, you can locate specific elements on a webpage and interact with them using Selenium.

Summary
Syntax for Locating by CSS Selector Usage
Method
Target Syntax
Example
Tag and ID
css=tag#id
css=input#email
Tag and Class
css=tag.class
css=input.inputtext
Tag and Attribute
css=tag[attribute=value]
css=input[name=lastName]
Tag, Class, and Attribute
css=tag.class[attribute=value]
css=input.inputtext[tabindex=1]











