First hello world

Document object model
also called DOM

Example:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
    </head>
    <body>
        Hello, world!
        </body>
    </html>
```

You can do headers

```html
<h1></h1>
```

Up to h6 for smallest inside the body.

There are two types of lists.

Ordered and unordered, check lists.html for example.

CSS styling can be linked to style an html file using <link rel="stylesheet" href="styles.css"> usually inside of <head>

There is "Specificity" which is heriarchy of specifications for style element

The specificity goes as follows:

1. inline
2. id
3. class
4. type

Viewport is the visible area of the web page, which can be controlled with CSS using `@media` queries.

Media queries allow you to apply styles based on the viewport size, enabling responsive design. For example:

````html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
    <syle>
    @media (min-width: 600px) {
      body {
        background-color: lightblue;
      }

    @media (max-width: 599px) {
      body {
        background-color: lightgreen;
      }
    </syle>
    </head>
    <body>
       <h1>Welcome to My Web Page!</h1>
        </body>
    </html>
```
Flexbox is a layout model that allows you to design a complex layout structure in a more efficient and predictable way than traditional models. It is particularly useful for aligning items in a container, distributing space, and handling responsiveness.

Bootstrap is a popular CSS framework that provides pre-designed components and responsive grid systems to help you build web pages quickly and efficiently. It includes styles for typography, forms, buttons, navigation, and more.

Sass is a CSS preprocessor that extends CSS with features like variables, nested rules, and mixins. It allows you to write more maintainable and organized stylesheets. Sass files are typically compiled into standard CSS files before being used in a web project. And browsers are not natively compiled to read Sass, so you need to use a tool like Node.js or a build system to compile Sass into CSS.
