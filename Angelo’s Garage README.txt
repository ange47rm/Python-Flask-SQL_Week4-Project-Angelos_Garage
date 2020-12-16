Angelo’s Garage documentation:




BASIC INFORMATION:


Angelo’s Garage is a web application meant to be for internal use only, by car dealership staff, to address some of the basic stock management needs of a car dealership.


Its simple structure includes a home/landing page, displaying basic information about the car dealership, a set of 3 navigation links (HOME, CARS, MANUFACTURERS), followed by contact details.


The landing page also features a grid of 6 car images. Such images, as well as the number of images, can be edited, however that would require that you modify the CSS selectors involved accordingly.


Lastly there is an ‘about’ section at the bottom featuring a description of the business and a relevant image.




MANAGEMENT FEATURES:


Other than the home page, the application allows you to access 2 other main sections of the application: the cars/products page and the manufacturers page. The information is pulled from an SQL database, and details about cars/products and manufacturers are displayed in a table format.


Such details can be edited, also rows can be added, allowing you to add a new car/product or manufacturer. Products/manufacturers can also be deleted if necessary.


The mileage database column will highlight the mileage in red for high mileage cars with over 150’000 km/miles, or green, if the mileage is particularly low (less than 25’000 km/miles). 


The manufacturers section uses hyperlinks to easily allow you to email your suppliers/manufacturers or visit their website.


IMPORTANT NOTES:
* In order to add a product from a specific manufacturer, you must ensure the manufacturer is added beforehand.
* If a manufacturer is deleted, all of its related cars/products will be deleted automatically from the database.




USAGE INFORMATION/INSTRUCTIONS:


The application uses the following technologies:


* Python 3
* Flask web framework (Python - HTML)
* PostgreSQL SQL database
* PsycoPG2 (Python - SQL)
* HTML5
* CSS


To start using the application, make sure your system is compatible with the above technologies.


1. The most recent version of the application is available at the following GitHub link, from which you will be able to clone the files to your local system.
Link: https://github.com/ange47rm/SQL-Python-Flask_Week4-Project-Angelos_Garage


2. From command prompt/terminal, create a database using the command: createdb database_name


3. In order to test functionality of the database, run the following command: psql -d database_name -f db/database_file.sql This command will run the sql file in the db folder, against the database you have created, creating the database tables defined in the sql file itself (you may need to run this twice the first time.


4. OPTIONAL: You can add some ‘test’ cars/products and manufacturers into such tables  by running the console.py file from your terminal/cmd prompt, making sure you are in the main directory of the application. Command: python3 console.py


5. From terminal/command prompt, navigate to the main directory of the application (angelos_garage_app folder by default) and use the following command to run Flask: run flask


6. By default, the  application will be hosted locally, can be accessed by visiting http://127.0.0.1:5000/ or http://localhost:5000/ in your internet browser (Google Chrome ideally).


7. You should finally be able to browse to the Home/Cars/Manufacturers pages and use the application.