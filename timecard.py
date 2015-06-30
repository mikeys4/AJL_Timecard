# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, g
import sqlite3

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = sqlite3.connect("users.db")

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/')
def hello_world():
	author = "Mike"
	return render_template('index.html', author=author)

@app.route('/signup', methods = ['POST'])
def signup():
	username = request.form['username']
	g.db.execute("INSERT INTO user_names VALUES (?)",[username])
	g.db.commit()
	return redirect('/')
	
if __name__ == '__main__':
	app.debug = True
	app.run()