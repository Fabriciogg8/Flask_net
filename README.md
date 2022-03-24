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

For this we will create the route named guestbook, and also the route guestbook/create_entry. 