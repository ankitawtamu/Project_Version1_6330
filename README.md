Customer Service Software System This is the initial vesrion of project where sign up, login, dashboard, service, complaints, success message page and log out were developed. 

username:ankita1@gmail.com password:12345

database: db.sqlite

virtual enviornment:penv (source penv/Scripts/activate)

This application works completely fine and databases were also fine for auth and main.But, at the time of testing ,this version was showing error in import function in test_main.py and testmock.py file. It was unable to import components from auth and main file.

So, later i developed a separate application(Final-Project_6330) with slightly different structure to accommodate Index, dashboard, service and success message page.

#Version1
$ export FLASK_APP=flaskr

$ export FLASK_ENV=development

$ flask run
