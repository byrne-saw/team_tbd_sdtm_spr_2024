###############################################################################
## JeoparDIY Flask Application  
## Team 2
##
## The **prefix.py** code is included to allow code to be developed within
## the **csel.io** environment.  There is a required prefix to be used when
## pages access the **csel.io** virtual machine from a local machine browser.
## 
###############################################################################

###############################################################################
## Import "prefix" code to make your app usable when running Flask either in 
## the csel.io virtual machine or running on a local machine.
## The module will create an app to use.
import prefix
import psycopg2
import json
from flask import jsonify

from flask import Flask, url_for
from flask import render_template
from markupsafe import escape

# create app to use in this Flask application
app = Flask(__name__)

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
# prefix.use_PrefixMiddleware(app)   

# test route to show prefix settings
@app.route('/prefix_url')  
def prefix_url():
    return 'The URL for this page is {}'.format(url_for('prefix_url'))

###############################################################################

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

# Game instructions
@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/gameplay')
def gameplay(): # will need to send in categories somehow...
    return render_template('gameplay.html')

@app.route('/player-names')
def player_names():
	return render_template('p2_names_categ.html')


# create Category table
def creating():
	conn = psycopg2.connect("postgres://tin_db_user:tTiToULPV8Lk0GywTYolmJYineD40MUb@dpg-co0ekkol5elc738o47p0-a/tin_db")
	cur = conn.cursor()
	cur.execute('''
	DROP TABLE IF EXISTS Category; 
    CREATE TABLE IF NOT EXISTS Category(
		Number int,
        CategName varchar(255)
        );
	''')
	conn.commit()
	conn.close()
	return "Category Table Successfully Created"


# insert values into Category table
def inserting():
	conn = psycopg2.connect("postgres://tin_db_user:tTiToULPV8Lk0GywTYolmJYineD40MUb@dpg-co0ekkol5elc738o47p0-a/tin_db")
	cur = conn.cursor()
	cur.execute('''
	INSERT INTO Category (Number, CategName)
	Values
	(1, 'MOUNTAIN HIGH'),
	(2, 'FROM THE FRENCH'),
	(3, 'BONDS OF COMMONALITY'),
	(4, 'RAP WORDS & PHRASES'),
	(5, 'NONFICTION'),
	(6, 'I LIKE THE CUT OF YOUR JOB')
	''')
	conn.commit()
	conn.close()
	return "Category Table Populated"


# flask route to fetch categories from the Category table
@app.route('/categories')
def get_categories():
	conn = psycopg2.connect("postgres://tin_db_user:tTiToULPV8Lk0GywTYolmJYineD40MUb@dpg-co0ekkol5elc738o47p0-a/tin_db")
	cur = conn.cursor()
	cur.execute('SELECT CategName FROM Category ORDER BY Number')
	categories = cur.fetchall()
	conn.close()
	return jsonify(categories)


# drop Category table from the database
@app.route('/db_drop')
def dropping():
	conn = psycopg2.connect("postgres://tin_db_user:tTiToULPV8Lk0GywTYolmJYineD40MUb@dpg-co0ekkol5elc738o47p0-a/tin_db")
	cur = conn.cursor()
	cur.execute('''
		DROP TABLE Category;
	''')
	conn.commit()
	conn.close()
	return "Category Table Successfully Dropped"


###############################################################################
# main driver function
if __name__ == '__main__':
	creating()
	inserting()
	# run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)

