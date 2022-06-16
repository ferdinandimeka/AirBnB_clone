# 0x01. AirBnB clone - Web static

## Concepts
For this project, students are expected to look at these concepts:

* HTML/CSS
* The trinity of front-end quality

# Background Context

Web static, what?
Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

* Create simple HTML static pages
* Style guide
* Fake contents
* No Javascript
* No data loaded from anything
During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

Before starting, please fork or clone the repository ``AirBnB_clone`` from your partner if you were not the owner of the previous project.

## Resources
Read or watch:

* [Learn to Code HTML & CSS (until “Creating Lists” included)](https://learn.shayhowe.com/html-css/)
* [Inline Styles in HTML](https://www.codecademy.com/article/html-inline-styles)
* [Specifics on CSS Specificity](https://css-tricks.com/specifics-on-css-specificity/)
* [CSS SpeciFishity](http://www.standardista.com/wp-content/uploads/2012/01/specificity3.pdf)
* [Introduction to HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)
* [MDN](https://developer.mozilla.org/en-US/)
* [center boxes](https://css-tricks.com/centering-css-complete-guide/)

# Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:

## General
* What is HTML
* How to create an HTML page
* What is a markup language
* What is the DOM
* What is an element / tag
* What is an attribute
* How does the browser load a webpage
* What is CSS
* How to add style to an element
* What is a class
* What is a selector
* How to compute CSS Specificity Value
* What are Box properties in CSS

# Requirements
## General
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is 
* Your code should be W3C compliant and validate with [W3C-Validator](https://github.com/holbertonschool/W3C-Validator)
* All your CSS files should be in styles folder
* All your images should be in images folder
* You are not allowed to use !important and id (#... in the CSS file)
* You are not allowed to use tags img, embed and iframe
* You are not allowed to use Javascript
* Current screenshots have been done on Chrome 56 or more.
* No cross browsers
* You have to follow all requirements but some margin/padding are missing - you should try to fit as much as you can to screenshots

## More Info

[image](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step1.png)

# Quiz questions
Hide

## Question #0
Is the following HTML markup valid?
```
<html></html>
```

(elements are correctly tagged, we don’t care about !Doctype here)

<b>Options</b>

* Yes
* No

<b>Answer</b>

* Yes

## Question #1
Is the following HTML markup valid?
```
<html>
    <head>
    </head>
    <body>
    </body>
</html>
```

(elements are correctly tagged, we don’t care about !Doctype here)

<b>Options</b>

* Yes
* No

<b>Answer</b>

* Yes

## Question #2
Is the following HTML markup valid?
```
<html>
    <head>
    </head>
    <body>
    <body>
</html>
```

(elements are correctly tagged, we don’t care about !Doctype here)

<b>Options</b>

* Yes
* No

<b>Answer</b>

* No
```
Tips:
Each HTML tag must be closed
```

## Question #3
Is the following HTML markup valid?
```
<html>
    <head>
    </head>
    <body>
        <img src="logo.png" />
    </body>
</html>
```

(elements are correctly tagged, we don’t care about !Doctype here)

<b>Options</b>

* Yes
* No

<b>Answer</b>

* Yes

```
Tips:
<img /> is an empty element
```

## Question #4
Is the following HTML markup valid?
```
<html>
    <head>
    </head>
    <body>
        <h1>Best <b>School</h1></b>
    </body>
</html>
```

(elements are correctly tagged, we don’t care about !Doctype here)

<b>Options</b>

* Yes
* No

<b>Answer</b>

* No
```
Tips:
“Always close something before opening a new thing”
```

## Question #5
Is the following HTML markup valid?
```
<html>
    <head>
    </head>
    <body>
        <h1>
            <a href="www.google.com'>Google</a>
        </h1>
    </body>
</html>
```
(elements are correctly tagged, we don’t care about !Doctype here)

<b>Options</b>
* Yes
* No

<b>Answer</b>

* No
```
Tips:
Number of quotes is important!
```

## Question #6
Is the following HTML markup valid?
```
<html>
    <head>
    </head>
    <body>
        <h1>
            <a href="www.google.com">Go to <b>Google</b>
        </h1>
    </body>
</html>
```

(elements are correctly tagged, we don’t care about !Doctype here)

<b>Options</b>

* Yes
* No

<b>Answer</b>

* No

## Question #7
Is following CSS syntax valid?
```
body {
    color: #FF0000;
}
```

<b>Options</b>

* Yes
* No

<b>Answer</b>

* Yes

## Question #8
Is following CSS syntax valid?
```
body {
    color: #FF0000;
}

* {
    font-size: 14px;
}
```

<b>Options</b>

* Yes
* No

<b>Answer</b>

* Yes
```
Tips:
[Universal selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Universal_selectors)
```

## Question #9
Is following CSS syntax valid?
```
body {
    color: #FF0000;
}

* {
    font-size: 14px;
    font-weight: 400
    text-align: center;
}
```

<b>Options</b>

* Yes
* No

<b>Answer</b>

* No
```
Tips:
Betty for CSS!
```

## Question #10
Is following CSS syntax valid?
```
body {
    color: #FF0000;
}

* {
    font-size: 14px;
    text-align: center;

    h1 {
        margin: 30px;
    }
}
```

<b>Options</b>

* Yes
* No

<b>Answer</b>

* No
```
Tips:
CSS vs SCSS
```

## Question #11
Is following CSS syntax valid?
```
body {
    color: #FF0000;
}

* {
    font-size: 14px;
    text-align: center;
    margin: 30px 12px 4px;
}
```

<b>Options</b>

* Yes
* No

<b>Answer</b>

* Yes
Tips:
```
margin and padding support 4 different syntaxes: margin
```

## Question #12
Is following CSS syntax valid?
```
body {
    color: #FF0000;
}

h1.title {
    font-size: 16px;
}
```

<b>Options</b>

* Yes
* No

<b>Answer</b>

* Yes

## Question #13
Is following CSS syntax valid?
```
body {
    color: #FF0000;
}

div.filters h2 {
    font-size: 16px;
}
```

<b>Options</b>

* Yes
* No

Question #14
Is following CSS syntax valid?
```
body {
    color: #FF0000;
}

div.filters p.title h2 span.text.big {
    font-size: 20px;
}
```


Yes


No

Question #15
Is following CSS syntax valid?
```
body {
    color: #FF0000;
}

h3,
div.full_text,
div.small_text h4,
div.filters p.title {
    font-size: 20px;
}
```

Yes


No

Question #16
Is following CSS syntax valid?
```
body {
    color: #FF0000;
}

h3,
div.full_text
div.small_text h4
div.filters p.title {
    font-size: 20px;
}
```

Yes


No

Tips:
, separates multiple selector, without it’s specific selector

Question #17
In the following code, is the text Best School red?

css:
```
h1 {
    color: red;
}
```

html:
```
<h1>Best School</h1>
```

Yes


No

Question #18
In the following code, is the text Best School red?

css:
```
h2 {
    color: red;
}
```

html:
```
<h1>Best School</h1>
```

Yes


No

Question #19
In the following code, is the text Best School red?

css:
```
h1.title {
    color: red;
}
```

html:
```
<h1>Best School</h1>
```

Yes


No

Question #20
In the following code, is the text Best School red?

css:
```
h1 div.title {
    color: red;
}
```

html:
```
<h1>Best School</h1>
```

Yes


No

Question #21
In the following code, is the text Best School red?

css:
```
h3 span.text,
h1,
div.title {
    color: red;
}
```

html:
```
<h1>Best School</h1>
```
Yes


No

Question #22
In the following code, is the text Best School red?

css:
```
h1 {
    color: green;
}

span.my_title {
    color: red;

```
html:

```
<h1>
    <span class="my_title">Best School</span>
</h1>
```

Yes


No

Tips:
[CSS selector math](http://www.standardista.com/wp-content/uploads/2012/01/specificity3.pdf)

Question #23
In the following code, is the text Best School red?

css:
```
h1 .my_title {
    color: green;
}

.my_title {
    color: red;
}
```

html:
```
<h1>
    <span class="my_title">Best School</span>
</h1>
```
Yes


No

Tips:
[CSS selector math](http://www.standardista.com/wp-content/uploads/2012/01/specificity3.pdf)


# W3C validator Testing
For HTML, CSS and SVG files

Based on 1 API:
- [Markup Validator Web Service API](https://validator.w3.org/docs/api.html)

## Requirements
- [Python 3](https://www.python.org/downloads/)
- [Requests: HTTP for Humans™](https://requests.readthedocs.io/en/master/index.html)

## Quickstart

Run the validator command from within

Single file:

```sh
./w3c_validator.py 6-index.html
```

```sh
./w3c_validator.py styles/3-header.css
```

Multiple files:

```sh
./w3c_validator.py 0-index.html 1-index.html styles/3-header.css
```

All errors are printed in `STDERR`; Exit status = # of errors (0 on success)

## Troubleshooting

- Error: `bad interpreter: No such file or directory`
If you get this error you might not have Python installed correctly; or the system [PATH](https://en.wikipedia.org/wiki/PATH_(variable)) might not be updated to reflect the installed Python version.

Assuming that Python 3 is indeed installed, you can try to run it like so:
```
python3 w3c_validator.py 0-index.html
```
- Error: `ModuleNotFoundError: No module named 'requests'`
If you get this error you do not have the module `requests` installed in your system.

You can install `requests` using pip:
```
python 3 -m pip install requests
```

If you don't have `pip` installed, you can get it [here](https://pypi.org/project/pip/).


# Tasks

## 0. Inline styling

Write an HTML page that displays a header and a footer.

Layout:

* Body:
  * no margin
  * no padding
* Header:
  * color #FF0000 (red)
  * height: 70px
  * width: 100%
* Footer:
  * acolor #00FF00 (green)
  * aheight: 60px
  * awidth: 100%
  * atext Best School center vertically and horizontally
  * always at the bottom at the page

Requirements:

* You must use the header and footer tags
* You are not allowed to import any files
* You are not allowed to use the style tag in the head tag
* Use inline styling for all your tags


<b>Repo:</b>

* GitHub repository: ``AirBnB_clone``
* Directory: ``web_static``
* File: [0-index.html](./0-index.html/)
 
## 1. Head styling

Write an HTML page that displays a header and a footer by using the style tag in the head tag (same as 0-index.html)

Requirements:

* You must use the header and footer tags
* You are not allowed to import any files
* No inline styling
* You must use the style tag in the head tag
* The layout must be exactly the same as 0-index.html

<b>Repo:</b>

* GitHub repository: ``AirBnB_clone``
* Directory: ``web_static``
* File: [1-index.html](./1-index.html/)
 
## 2. CSS files

Write an HTML page that displays a header and a footer by using CSS files (same as 1-index.html)

Requirements:

* You must use the header and footer tags
* No inline styling
* You must have 3 CSS files:
   * styles/2-common.css: for global style (i.e. the body style)
   * styles/2-header.css: for header style
   * styles/2-footer.css: for footer style

The layout must be exactly the same as 1-index.html

<b>Repo:</b>

* GitHub repository: ``AirBnB_clone``
* Directory: ``web_static``
* File: 2-index.html, styles/2-common.css, styles/2-header.css, styles/2-footer.css
 
## 3. Zoning done!

Write an HTML page that displays a header and footer by using CSS files (same as 2-index.html)

Layout:

* Common:
  * no margin
  * no padding
  * font color: #484848
  * font size: 14px
  * font family: Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;
icon in the browser tab

* Header:
  * color: white
  * height: 70px
  * width: 100%
  * border bottom 1px #CCCCCC
  * logo align on left and center vertically (20px space at the left)

* Footer:
  * color white
  * height: 60px
  * width: 100%
  * border top 1px #CCCCCC
  * text Best School center vertically and horizontally
  * always at the bottom at the page

Requirements:

* No inline style
* You are not allowed to use the img tag
* You are not allowed to use the style tag in the head tag
* All images must be stored in the images folder
* You must have 3 CSS files:

  * styles/3-common.css: for the global 
  * style (i.e body style)
  * styles/3-header.css: for the header style
  * styles/3-footer.css: for the footer style


<b>Repo:</b>

* GitHub repository: ``AirBnB_clone``
* Directory: ``web_static``
* File: 3-index.html, styles/3-common.css, styles/3-header.css, styles/3-footer.css, images/
 
## 4. Search!

Write an HTML page that displays a header, footer and a filters box with a search button.

Layout: (based on 3-index.html)

* Container:
  * between header and footer tags, add a div:
	  * classname: container
	  * max width 1000px
	  * margin top and bottom 30px - it should be 30px under the bottom of the header (screenshot)
	  * center horizontally
* Filter section:
  * tag section
  * classname filters
  * inside the .container
  * color white
  * height: 70px
  * width: 100% of the container
  * border 1px #DDDDDD with radius 4px
* Button search:
  * tag button
  * text Search
  * font size: 18px
  * inside the section filters
  * background color #FF5A5F
  * text color #FFFFFF
  * height: 48px
  * width: 20% of the section filters
  * no borders
  * border radius: 4px
  * center vertically and at 30px of the right border
  * change opacity to 90% when the mouse is on the button

Requirements:

* You must use: header, footer, section, button tags
* No inline style
* You are not allowed to use the img tag
* You are not allowed to use the style tag in the head tag
* All images must be stored in the images folder
* You must have 4 CSS files:
  * styles/4-common.css: for the global style (body and .container styles)
  * styles/3-header.css: for the header style
  * styles/3-footer.css: for the footer style
  * styles/4-filters.css: for the filters style
4-index.html won’t be W3C valid, don’t worry, it’s temporary


<b>Repo:</b>

GitHub repository: ``AirBnB_clone``
Directory: ``web_static``
File: 4-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/4-filters.css, images/
 
## 5. More filters

Write an HTML page that displays a header, footer and a filters box.

Layout: (based on 4-index.html)

* Locations and Amenities filters:
  * tag: div
  * classname: locations for location tag and amenities for the other
  * inside the section filters (same level as the button Search)
  * height: 100% of the section filters
  * width: 25% of the section filters
  * border right #DDDDDD 1px only for the first left filter
  * contains a title:
     * tag: h3
     * font weight: 600
     * text States or Amenities
  * contains a subtitle:
     * tag: h4
     * font weight: 400
     * font size: 14px
     * text with fake contents

Requirements:

* You must use: header, footer, section, button, h3, h4 tags
* No inline style
* You are not allowed to use the img tag
* You are not allowed to use the style tag in the head tag
* All images must be stored in the images folder
* You must have 4 CSS files:
  * styles/4-common.css: for the global style (body and .container styles)
  * styles/3-header.css: for the header style
  * styles/3-footer.css: for the footer style
  * styles/5-filters.css: for the filters style


<b>Repo:</b>

* GitHub repository: ``AirBnB_clone``
* Directory: ``web_static``
* File: 5-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/5-filters.css, images/
 
## 6. It's (h)over

Write an HTML page that displays a header, footer and a filters box with dropdown.

Layout: (based on 5-index.html)

* Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter div:
  * tag ul
  * classname popover
  * text should be fake now
  * inside each div
  * not displayed by default
  * color #FAFAFA
  * width same as the div filter
  * border #DDDDDD 1px with border radius 4px
  * no list display
  * Location filter has 2 levels of ul/li:
    * state -> cities
    * state name must be display in a h2 tag (font size 16px)

Requirements:

* You must use: header, footer, section, button, h3, h4, ul, li tags
* No inline style
* You are not allowed to use the img tag
* You are not allowed to use the style tag in the head tag
* All images must be stored in the images folder
* You must have 4 CSS files:
  * styles/4-common.css: for the global style (body and .container styles)
  * styles/3-header.css: for the header style
  * styles/3-footer.css: for the footer style
  * styles/6-filters.css: for the filters style
 

<b>Repo:</b>

* GitHub repository: ``AirBnB_clone``
* Directory: ``web_static``
* File: 6-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, images/
 
## 7. Display results

Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on 6-index.html)

* Add Places section:
  * tag: section
  * classname: places
  * same level as the filters section, inside .container
  * contains a title:
    * tag: h1
    * text: Places
    * align in the top left
    * font size: 30px
  * contains multiple “Places” as listing (horizontal or vertical) describe by:
    * tag: article
    * width: 390px
    * padding and margin 20px
    * border #FF5A5F 1px with radius 4px
    * contains the place name:
      * tag: h2
      * font size: 30px
      * center horizontally

Requirements:

* You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
* No inline style
* You are not allowed to use the img tag
* You are not allowed to use the style tag in the head tag
* All images must be stored in the images folder
* You must have 5 CSS files:
  * styles/4-common.css: for the global style (i.e. body and .container styles)
  * styles/3-header.css: for the header style
  * styles/3-footer.css: for footer style
  * styles/6-filters.css: for the filters style
  * styles/7-places.css: for the places style


<b>Repo:</b>

* GitHub repository: ``AirBnB_clone``
* Directory: ``web_static``
* File: 7-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/7-places.css, images/
 
## 8. More details

Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.

Layout: (based on 7-index.html)

Add more information to a Place article:

* Price by night:
  * tag: div
  * classname: price_by_night
  * same level as the place name
  * font color: #FF5A5F
  * border: #FF5A5F 4px rounded
  * min width: 60px
  * height: 60px
  * font size: 30px
  * align: the top right (with space)
* Information section:
  * tag: div
  * classname: information
  * height: 80px
  * border: top and bottom #DDDDDD 1px
  * contains (align vertically):
    * Number of guests:
      * tag: div
      * classname: max_guest
      * width: 100px
      * fake text
      * [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_group.png)
    * Number of bedrooms:
      * tag: div
      * classname: number_rooms
      * width: 100px
      * fake text
      * [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bed.png)
    * Number of bathrooms:
      * tag: div
      * classname: number_bathrooms
      * width: 100px
      * fake text
      * [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bath.png)
* User section:
  * tag: div
  * classname: user
  * text Owner: <fake text>
  * Owner text should be in bold
* Description section:
  * tag: div
  * classname: description

Requirements:

* You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
* No inline style
* You are not allowed to use the img tag
* You are not allowed to use the style tag in the head tag
* All images must be stored in the images folder
* You must have 5 CSS files:
  * styles/4-common.css: for the global style (i.e. body and .container styles)
  * styles/3-header.css: for the header style
  * styles/3-footer.css: for the footer style
  * styles/6-filters.css: for the filters style
  * styles/8-places.css: for the places style


<b>Repo:</b>

* GitHub repository: ``AirBnB_clone``
* Directory: ``web_static``
* File: 8-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/8-places.css, images/
 
## 9. Full details
#advanced
Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on 8-index.html)

Add more information to a Place article:

* List of Amenities:
  * tag div
  * classname amenities
  * margin top 40px
  * contains:
    * title:
      * tag h2
      * text Amenities
      * font size 16px
      * border bottom #DDDDDD 1px
    * list of amenities:
      * tag ul / li
      * no list style
      * icons on the left: [Pet friendly](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_pets.png), [TV](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_tv.png), [Wifi](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_wifi.png), etc… feel free to add more
* List of Reviews:
  * tag div
  * classname reviews
  * margin top 40px
  * contains:
    * title:
      * tag h2
      * text Reviews
      * font size 16px
      * border bottom #DDDDDD 1px
    * list of review:
      * tag ul / li
      * no list style
      * a review is described by:
        * h3 tag for the user/date description (font size 14px). Ex: “From Bob Dylan the 27th January 2017”
        * p tag for the text (font size 12px)

Requirements:

* You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
* No inline style
* You are not allowed to use the img tag
* You are not allowed to use the style tag in the head tag
* All images must be stored in the images folder
* You must have 5 CSS files:
  * styles/4-common.css: for the global style (body and .container styles)
  * styles/3-header.css: for the header style
  * styles/3-footer.css: for the footer style
  * styles/6-filters.css: for the filters style
  * styles/100-places.css: for the places style


<b>Repo:</b>

* GitHub repository: ``AirBnB_clone``
* Directory: ``web_static``
* File: 100-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/100-places.css, images/
 
## 10. Flex #advanced
Improve the Places section by using [Flexible](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox) boxes for all Place articles

[Flexbox Froggy](http://flexboxfroggy.com/)

<b>Repo:</b>

* GitHub repository: ``AirBnB_clone``
* Directory: ``web_static``
* File: 101-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/101-places.css, images/
 
## 11. Responsive design #advanced
Improve the page by adding [responsive design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design) to display correctly in mobile or small screens.

Examples:

* no horizontal scrolling
* redesign search bar depending of the width
* etc.

<b>Repo:</b>

* GitHub repository: ``AirBnB_clone``
* Directory: ``web_static``
* File: 102-index.html, styles/102-common.css, styles/102-header.css, styles/102-footer.css, styles/102-filters.css, styles/102-places.css, images/
 
## 12. Accessibility #advanced
Improve the page by adding [Accessibility](https://developer.mozilla.org/en-US/docs/Learn/Accessibility) support

Examples:

* Colors contrast
* Header tags
* etc.

<b>Repo:</b>

* GitHub repository: ``AirBnB_clone``
* Directory: ``web_static``
* File: 103-index.html, styles/103-common.css, styles/103-header.css, styles/103-footer.css, styles/103-filters.css, styles/103-places.css, images/