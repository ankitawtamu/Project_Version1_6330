from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . models import Store, User
from flask_login import login_user
from flask_sqlalchemy import SQLAlchemy
from . import db
from sqlalchemy import MetaData
from sqlalchemy import create_engine, MetaData, Table,Column, Integer, String
from sqlalchemy.orm import sessionmaker
import sqlite3 as sql
import sqlite3
from datetime import datetime

main = Blueprint('main', __name__)


con = sqlite3.connect('./flaskr/db.sqlite')



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
    

@main.route('/service',methods = ['POST', 'GET'])
def service():
    return render_template('service.html')

@main.route('/complaint',methods = ['POST', 'GET'])
def complaint():
    return render_template('complaint.html')    


@main.route('/delete')
def delete():
    return render_template('delete.html')

@main.route('/update')
def update():
    return render_template('update.html')



  

@main.route('/addcomplaint', methods = ['POST', 'GET'])
def addcomplaint():
    name = request.form.get('name')
    type = request.form.get('type')
   

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_store = Store(name=name,type=type)

    # add the new user to the database
    db.session.add(new_store)
    db.session.commit()
    message = "added successfully"
    return render_template("message_added.html",message = message)



@main.route('/deletecomplaint', methods = ['POST', 'GET'])
def deletecomplaint():
    if request.method == 'POST':
        try:

            id = request.form['id']

            new_store = Store.query.filter_by(id=id).one()
            db.session.delete(new_store)
            db.session.commit()
            message = "Complain deleted successfully!"

        except:
            message = "Error in deleting complain"

        finally:

            return render_template("msg_update_delete.html", message=message)

# list entire table
@main.route('/list')
def list():
    store = Store.query.all()
   
    return render_template("list.html",store=store)   

@main.route('/updatecomplaint', methods = ['POST', 'GET'])
def updatecomplaint():
    if request.method == 'POST':
        try:
            
            id = request.form['id']
            name = request.form.get('name')
            type = request.form.get('type')

            #x = Store.query.filter_by(id=id).one()
            x=Store(id=id,name=name,type=type)

            db.session.merge(x)
            db.session.commit()
          
            message = "Complain updated successfully!"

        except:
            message = "Error in updating complain"

        finally:

            return render_template("msg_update_delete.html", message=message)





