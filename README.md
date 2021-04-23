Customer Service Software System This is the initial vesrion of project where sign up, login, dashboard, service, complaints, success message page and log out were developed. 

username:ankita1@gmail.com password:12345

database: db.sqlite

virtual enviornment:penv (source penv/Scripts/activate)

This version was showing error in import function in test_main.py and testmock.py file. So , it could not be used for testing although the application works perfectly.

Hence i developed another version(Final-Project_6330) without auth and login to successfully test it.

$ export FLASK_APP=flaskr

$ export FLASK_ENV=development

$ flask run
