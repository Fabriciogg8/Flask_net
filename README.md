# FLASK

This is a repository working with Flask. 

## Views

We have two different **views**, one that corresponds to the application views that are located in the **route.py** file, and on the other hand we have the administrator views that are located in the **admin_routes.py** file.

This two files are called from the dunder init file.

## Templates

We also have two diferent folders inside of templates. One folder that we call **admin**, is the one who contains all the admin templates. On the other hand, the folder named **public** is the folder that contains all the public templates. 

## Static

Next we create the **static** directory, where we have three more folders **CSS**, **JS** and **IMG**.
Inside css we create the style.css file where we are going to do all the styling. And also within js we generate the app.js file where we will create all the javascript code. For last we add the images to the folder of images. 

We add the files generated in this folders to the base.html file, using **url_for**.

Later on, we create two folders called template. One inside of admin, and one inside of public. 

We are going to use bootstrap, so we generate the **public_template.html** and the **admin_template.html**, and we add the starting template from bootstrap to these files. Also we add the custom CSS and JS that we previously generated.

## Jinja

We start by creating a new route, inside our public routes, called jinja. This route is going to render a **variable** called name, and we also add diferent types of python **data types (list, dict, tuple, etc)**
Then we create the html, to display this view. And inside the html we start to play with the Jinja sintax to display the diferent type of data. 

We can create our own customized filters to work with jinja, for this we create the **filters.py** file, the we called from the routes file and we can see the results in the jinja file.

Next, we create the **macros** folder, inside of templates. Here we create a file called input_macro.html, so we can generate a macros that we can use in both, admin and user templates file. To do so, we need to import this file from the html we need it. 

## Forms

The first thing is to create a new route inside our public routes, called sign-up. Next, we create the html file with the same name (sign_up). 

Inside the html file we create a **form**. This form has an **action** attribute that takes a **URL** for sending that form to somewhere. The **method** that we use when we decide to send information to the server is **POST**, so we have to put it in the attribute of the form. For the form **inputs**, we need to create a **name** attribute for each input we're going to use, so that we can access the input's value submited.

After we finish the form, we go to our route and add the **POST method**, so the route knows that is allowed to receive data. For us to be able to receive the data, we need to import **request** from flask. At the same time we import **redirect** so we can used later, allowing us to redirect the user to other page if we want it to.  

We see in our route function that we can create an if statement for the POST method. Then we can save in a variable the data in the **request.form** (this is a dict, so we can access the values inside the request.form, in different forms as shown in the function). 


## Dinamic URL 

The first is to create a new route, that we call profile for now. The we create the html file. We came back to the routes and we add a **variable** to the **path** to our page, so we can access our own profile page, with wathever our name is. I add a file called data.py where we have the dummy data for using in the route. 

We create a variable called name where we store the data from the user, if the user is in the data list. Then we pass this variable trough the render_template and use it to display the information in the profile template.
We can use Jinja in order to differentiate if the user is in the data or not, and display different formats.

The we create another example where we have **multiple variables** in the path of our route. 

## JSON

We are going to send and receive **JSON**. In order to do so, we start for creating a new route called /json. We will be returning a simple string with a **HTTP status code**.We can try this out in POSTMAN.

When we use POSTMAN we can send information in JSON format to our route. To get this information we use **request.get_json()**. This converts the JSON file to a Python dictionary. 

Also we can send JSON from our route to the client, to do so we have to import from flask **jsonify** and **make_response**. To doing this we create a python dictonary inside the json route. 

## AJAX 

For this we will create the route named guestbook, and also the route guestbook/create_entry. Then we create the html guestbook.html in wich we create a form, with a button who triggers a function named **submit_entry()**.

Then we create the **script tags** inside guestbook.html, where we create the function submit_entry with javascript. This function gets the values inside the inputs and in the first implementation only prints the values trough the console via console.log. 

After that, we go to the route guestbook/create_entry, where we will be handle the request from javascript. And also, we will responde with JSON. In the html, we are back to our JS and we add the **fetch API**. We have to introduce some attributes to fetch, the first one is the url, so we ca use **window.origin**, that will grab in this case http://127.0.0.1:5000/, and then add the rest of the route where we want to use fetch. 

***Corollary:*** To simplify the fetch url, you can simply use a single forward slash ( "/" ) to signify that your URL is relative to your origin. So in this case, no need for the window.origin stuff. Your request URL could be "/guestbook/create-entry". Only time fully qualified URLs matter is if you're making cross-site requests -- say, if your API server is sitting on a different domain than your web server.

After we have te route where we are going to post some data, we have to create a new Javascript object, as a second attribute.

We use .then to receive the response from the page and we do a console.log to see what the response of the page was, after we made the post request.

## Query string

We create a new route called query, and use the request object, to work with query strings. We will create a variable called args that will contain **request.args**. If we put this in a print, and then we go to our browser and we insert in the url the route and a query (http://127.0.0.1:5000/query?bar=bar&baz=baz), we get in the terminal an **InmutableMultiDict**. We can work with this dict, and print the keys and values with a for loop. 

Another object we can use is **request.query_string**, we can print it out and we will see the query we introduce in the url, printed in the terminal. 

## Config

Flask configutation, it's a way of creating some default keys and values which contain important information that we won't be able to use in our app, like Secret keys, API keys. In definitive any kind of information that is sensitive and you don't want to hard code into your app. 

If we use the index route, and print **app.config** the terminal will show us the config dictionary. These values are the default values set by flask, and we can accedd them from any part of our application.    

That was only to experiment. We will create a new file **config.py** in our root folder, where we will set all de configuration variables. There many ways to do it, but we will create a class for setting the variables. Also then, we will continuing by creating three more classes (Testing, Development, and ProductionConfig) that will be inheriting from the first.

After we finish with our configuration file, we need to attach him to our app object. Then we can choose which of the classes we created will be used. We can do it, by using an if statement, so it will change the class depending of the environment we are working on. 

***Corollary:*** To change the enviroment in CMDER console we can use: **set FLASK_ENV=development** , in other terminal we can use export. 

## Uploading files

As always we create a new route, an we named upload_image. Also we create a new html, called upload_image.html. Inside of this html, we put a form where the besides action and method we insert **enctype**. The enctype attribute can be used only if method="post". Then inside the form we need an input with **type file**. 

In the route we need to make the logic for the request of the file, id the used method is POST. Then we create a new folder inside of static/img called uploads, where we are going to store the images. Outside the route function we can set a new key called **['IMAGE_UPLOADS']** to the config dict. In this key, we are going to declare the **absolute path** to the folder where we want to save the images. One way to do this, is in our terminal moving ourselves to this directory in use the command **pwd**.  

We have to ensure that the file has a filename, the file type is equal to the one we specify, the filename is secure and the size of file is within a reasonable limit. We need to import werkzeug that is the responsable to retunr a secure version of the filename. For the resize image problem, I used the pillow library. 