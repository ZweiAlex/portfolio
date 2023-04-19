from flask import Flask, render_template, request, flash, session
from flask_session.__init__ import Session
import datetime
app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)


@app.route('/')
def index():
    dt = datetime.datetime.now()
    now = dt.strftime("%Y-%m-%d %H:%M")
    return render_template('index.html', date_time=now)


@app.route('/resume')
def resume():
    dt = datetime.datetime.now()
    now = dt.strftime("%Y-%m-%d %H:%M")
    return render_template('resume.html', date_time=now)


@app.route('/website')
def website():
    dt = datetime.datetime.now()
    now = dt.strftime("%Y-%m-%d %H:%M")
    return render_template('website.html', date_time=now)


@app.route('/contact-me')
def contact_me():
    dt = datetime.datetime.now()
    now = dt.strftime("%Y-%m-%d %H:%M")
    return render_template('contact-me.html', date_time=now)