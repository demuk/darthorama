from app import app
from flask import render_template, redirect, url_for



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	
	return render_template('signin.html')


@app.route('/contact')
def contact():

    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')
