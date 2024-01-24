# Selenium Form:
An HTML (Hypertext Markup Language) page is a document that is interpreted by web browsers to display content 
on the internet. It consists of various elements that structure the content and provide different types of 
functionality.Here are some of the basic elements and their functions:

    <!DOCTYPE html>: 
This is the document type declaration and indicates that the document is an HTML5 document.

    <html>: 
This is the root element of an HTML page and contains all other elements.

    <head>: 
This element contains metadata about the document such as the title, keywords, and author.

    <title>: 
This element specifies the title of the document, which is displayed in the browser's title bar and may be used by 
search engines to index the page.

    <body>: 
This element contains the main content of the page such as text, images, and videos.

    <h1> to <h6>: 
These elements are used to create headings of different sizes, with h1 being the largest and h6 being the smallest.

    <p>: 
This element is used to create paragraphs of text.

    <a>: 
This element creates hyperlinks that allow users to navigate to other pages on the web.

    <img>: 
This element is used to embed images in the page.

    <ul> and <li>: 
These elements are used to create unordered lists.

    <ol> and <li>: 
These elements are used to create ordered lists.

    <div>: 
This element is used to group together other elements and apply styles to them.

These are just some of the basic elements used in an HTML page. There are many more elements and attributes 
available to create more complex and interactive web pages.


# HTML Document Structure:
    <!DOCTYPE html>: Declares the HTML version being used (HTML5 in this case).
    <html>: The root element of an HTML page.
    <head>: Contains meta-information about the HTML document (not displayed on the page).
    <title>: Sets the title of the HTML document, displayed on the browser's title bar or tab.
    <body>: Contains the content of the HTML document.

Example:

    html
    Copy code
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Web Page</title>
    </head>
    <body>
        <!-- Content goes here -->
    </body>
    </html>


# Text and Headings:
    <p>: Represents a paragraph.
    <h1>, <h2>, ..., <h6>: Heading elements, where <h1> is the largest and <h6> is the smallest.
    Example:

        html
        Copy code
        <p>This is a paragraph.</p>
        <h1>This is a Heading 1</h1>

# Links and Images:
    <a>: Defines a hyperlink.
    href: Specifies the URL of the linked page.
    <img>: Embeds an image.
    src: Specifies the source URL of the image.
    alt: Provides alternative text for accessibility.
    Example:

        <a href="https://www.example.com">Visit Example.com</a>
        <img src="image.jpg" alt="Description of the image">

# Lists:
    <ul>: Represents an unordered list.
    <ol>: Represents an ordered list.
    <li>: Represents a list item.
    Example:

        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
        </ul>
        
        <ol>
            <li>First</li>
            <li>Second</li>
        </ol>


# Tables:
    <table>: Represents a table.
    <tr>: Represents a table row.
    <td>: Represents a table cell (data).
    Example:

    <table>
        <tr>
            <td>Row 1, Cell 1</td>
            <td>Row 1, Cell 2</td>
        </tr>
        <tr>
            <td>Row 2, Cell 1</td>
            <td>Row 2, Cell 2</td>
        </tr>
    </table>


# Attributes and IDs:
    class: Specifies one or more class names for styling.
    id: Specifies a unique identifier for an element.
    Example:


    <p class="important">This is an important paragraph.</p>
    <div id="uniqueElement">This is a unique element.</div>


# Forms:
    <form>: Represents an HTML form.
    <input>: Represents an input field.
    <button>: Represents a clickable button.
    Example
        <form action="/submit" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username">
            <button type="submit">Submit</button>
        </form>

These are just some fundamental elements and concepts in HTML. HTML provides a rich set of tags for 
structuring content, and it works together with other web technologies to create dynamic and visually 
appealing web pages. Feel free to ask for more specific details or examples if needed!
