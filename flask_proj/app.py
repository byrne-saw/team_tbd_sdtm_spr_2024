###############################################################################
## JeoparDIY Flask Application  
## Team 2
##
###############################################################################

import os

import psycopg2
import json
from flask import jsonify

from flask import Flask, url_for
from flask import render_template
from markupsafe import escape


# create Category table
def create_db_tables():
	conn = psycopg2.connect("postgres://tin_db_user:tTiToULPV8Lk0GywTYolmJYineD40MUb@dpg-co0ekkol5elc738o47p0-a/tin_db")
	cur = conn.cursor()
	cur.execute('''
	DROP TABLE IF EXISTS Category; 
    CREATE TABLE Category(
		Number int,
		CategName varchar(255)
        );
	''')
	conn.commit()
	conn.close()
	return "Category Table Successfully Created"


# insert values into Category table
def insert_data_into_dbtables():
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


# create app to use in this Flask application
#app = Flask(__name__)
def create_app():
	create_db_tables()
	insert_data_into_dbtables()
	app = Flask(__name__)
	
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
	
	@app.route('/categories')
	def get_categories():
		conn = psycopg2.connect("postgres://tin_db_user:tTiToULPV8Lk0GywTYolmJYineD40MUb@dpg-co0ekkol5elc738o47p0-a/tin_db")
		cur = conn.cursor()
		cur.execute('SELECT Number, CategName FROM Category ORDER BY Number')
		categories = cur.fetchall()
		conn.close()
		# Construct a list of dictionaries representing categories
		categories_list = []
		for category in categories:
			category_dict = {
				'Number': category[0],
				'CategName': category[1]
			}
			categories_list.append(category_dict)
		# Return the list of categories as JSON
		return jsonify(categories_list)

	
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
	
	
	return app
	
app = create_app()
app.config['DEBUG'] = os.environ.get('DEBUG', True)
