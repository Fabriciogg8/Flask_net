# Flask_net
Social net created with Flask

## Views

We have two different **views**, one that corresponds to the application views that are located in the **route.py** file, and on the other hand we have the administrator views that are located in the **admin_routes.py** file.

This two files are called from the dunder init file.

## Templates

We also have two diferent folders inside of templates. One folder that we call **admin**, is the one who contains all the admin templates. On the other hand, the folder named **public** is the folder that contains all the public templates. 

## STATIC

Next we create the **static** directory, where we have three more folders **CSS**, **JS** and **IMG**.
Inside css we create the style.css file where we are going to do all the styling. And also within js we generate the app.js file where we will create all the javascript code. For last we add the images to the folder of images. 

We add the files generated in this folders to the base.html file, using **url_for**.

Later on, we create two folders called template. One inside of admin, and one inside of public. 

We are going to use bootstrap, so we generate the **public_template.html** and the **admin_template.html**, and we add the starting template from bootstrap to these files. Also we add the custom CSS and JS that we previously generated.