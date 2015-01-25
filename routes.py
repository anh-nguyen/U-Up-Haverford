from flask import Flask, render_template, request

# all the imports
import sqlite3, re
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

from contextlib import closing

from flask.ext.socketio import SocketIO, emit


# configuration
DATABASE = '/tmp/UUp.db'
DEBUG = True
SECRET_KEY = 'StuD BuDs'
USERNAME = 'admin'
PASSWORD = 'default'
SESSION_TYPE = 'filesystem'
 
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
#socketio = SocketIO(app) 
 
def connect_db():
	return sqlite3.connect('/tmp/UUp.db')

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

@app.route('/')
def home():
	cur = g.db.execute('select name, activity, location, status from entries order by id desc')
	entries = [dict(name=row[0], activity=row[1], location=row[2], status=row[3]) for row in cur.fetchall()]
	return render_template('home.html', entries=entries)

@app.route('/joinin', methods=['GET', 'POST'])
def joinin():
	if request.method == 'POST':
		# NOTE: we no longer need to check the data fields because the html template has already done that
		# get user's IP
		user_ip = request.remote_addr
		# database stuff
		g.db.execute('insert into entries (name, email, location, activity, status, ip) values (?, ?, ?, ?, ?, ?)',				[request.form['name'].title(), request.form['email'], request.form['location'], request.form['activity'], request.form['status'], user_ip])
		g.db.commit()
		session['name'] = request.form['name']
		session['email'] = request.form['email']
		session['ip'] = user_ip
		return redirect(url_for('home'))
	return render_template('joinin.html')
	
@app.route('/leave', methods=['GET', 'POST'])
def leave():
	if request.method == 'POST':
		print "hello"
		user_ip = request.remote_addr
		print "user ip" +  user_ip
		g.db.execute('delete from entries where ip= ?', [user_ip])
		g.db.commit()
		return redirect(url_for('home'))
	print "not posting"
	return render_template('leave.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

if __name__ == '__main__':
	app.database = '/tmp/UUp.db'
	app.secret_key = 'StuD BuDs'	
	app.run(debug=True, host="0.0.0.0")
	#socketio.run(app, host="0.0.0.0")
