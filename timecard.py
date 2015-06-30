# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, g
import sqlite3

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = sqlite3.connect("timecards.db")

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

@app.route('/submit_paycheck', methods = ['POST'])
def submit_paycheck():
	Employee = request.form.get('Employee')
	EmployeeID = 1
	if Employee == 'Rob':
		EmployeeID = 1
	elif Employee == 'Rick':
		EmployeeID = 2
	elif Employee == 'Mike':
		EmployeeID = 3
	Date = request.form.get('Date')
	TimeIn = request.form.get('TimeIn')
	TimeOut = request.form.get('TimeOut')
	RegHours = request.form.get('RegHours')
	PtFiveTime = request.form.get('PtFiveTime')
	TwoXTime = request.form.get('TwoXTime')
	Sick = request.form.get('Sick')
	Vac = request.form.get('Vac')
	Holiday = request.form.get('Holiday')
	g.db.execute("INSERT INTO timecards (EmployeeID, WorkDay, TimeIn, TimeOut, RegHours, PtFiveTime, TwoXTime, Sick, Vac, Holiday) VALUES (?,?,?,?,?,?,?,?,?,?);", (EmployeeID, Date, TimeIn, TimeOut, RegHours, PtFiveTime, TwoXTime, Sick, Vac, Holiday))
	g.db.commit()
	return redirect('/')
	
if __name__ == '__main__':
	app.debug = True
	app.run()