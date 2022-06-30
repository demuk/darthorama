from app import app
from flask import render_template, redirect, url_for, request, flash
from app import app, db



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user=User(username=request.form['username'],email=request.form['email'],password_hash=generate_password_hash(request.form['password']))
        db.session.add(user)
        db.session.commit()
        return render_template('signin.html')
        flash('Your account has been created!', 'success')
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	
	return render_template('signin.html')


@app.route('/contact')
def contact():

    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')
