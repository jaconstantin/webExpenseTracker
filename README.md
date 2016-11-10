# webExpenseTracker

This project deals with the creation of a Web Based Expense Tracker Program. The objective is to allow different users to log in to their account, start recording their expense data, and view them at a later time. In contrast to the C++ version of this project, an HTML/CSS/javascript web page will be used as the UI for this project. A MySQL server will be at the backend of this application to store all data.  Furthermore, I am planning to use the query capabilities of MySQL in returning/summarizing/grouping a large amount of expenditure data. I am also planning to use Python or Django for the server side scripting, and maybe add chart/plot capabilities in the future.

-----------------------
Current progress
-----------------------
I decided to go with Django framework to be able to develop the client side UI and server side application. I have finished setting up the JCET django project. MySQL server is integrated to the Django project through the migration process, and I have tested that I can access the database through the django database API. I used django version 1.8.9, since I think that the latest version 1.10.3 has some issues with MySQL.

I have also finished integrating my sample web pages: home.html and input.html to the django project. It took quite a while to properly set up the static files, so that the web page can be rendered properly.

I will now be working to add the capabilities to add/view database entries through the web page.

------------------------
OLD Update Progress Logs
-------------------------
This project is at the early stage of its development. I am still working on the Web Page for the project. Currently, it features a decent amount of interactivity in the HOME and INPUT page. I have also built user input checking on javascript. I have the MySQL server and scripts up and running, but is currently not uploaded here. I will continue to log the changes here until the completion of the project.


