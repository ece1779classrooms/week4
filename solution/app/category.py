from flask import render_template, redirect, url_for, request, g
from app import webapp

import mysql.connector

from app.config import db_config

def connect_to_database():
    return mysql.connector.connect(user=db_config['user'], 
                                   password=db_config['password'],
                                   host=db_config['host'],
                                   database=db_config['database'])

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@webapp.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@webapp.route('/category',methods=['GET'])
# Display an HTML list of all category.
def category_list():
    cnx = get_db()

    cursor = cnx.cursor()

    query = '''SELECT * FROM category'''

    cursor.execute(query)
    
    return render_template("category/list.html",title="Category List", cursor=cursor)


@webapp.route('/category/create',methods=['GET'])
# Display an empty HTML form that allows users to define new student.
def category_create():
    return render_template("category/new.html",title="New Category")

@webapp.route('/category/create',methods=['POST'])
# Create a new student and save them in the database.
def category_create_save():
    name = request.form.get('name',"")

    cnx = get_db()
    cursor = cnx.cursor()


    query = ''' INSERT INTO category (name)
                       VALUES (%s)'''

    cursor.execute(query,(name,))
    cnx.commit()
    
    return redirect(url_for('category_list'))



@webapp.route('/category/delete/<int:id>',methods=['POST'])
# Deletes the specified student from the database.
def category_delete(id):
    cnx = get_db()
    cursor = cnx.cursor()

    query = "DELETE FROM category WHERE id = %s"
    
    cursor.execute(query,(id,))
    cnx.commit()

    return redirect(url_for('category_list'))

