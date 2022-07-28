from app import app
from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models import Post, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user,login_required,logout_user
import string
import secrets
import os



@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        alphabet = string.ascii_letters + string.digits
        user_key = ''.join(secrets.choice(alphabet) for i in range(32))
        user=User(username=request.form['username'],user_key=user_key,email=request.form['email'],
            password_hash=generate_password_hash(request.form['password']))
        db.session.add(user)
        db.session.commit()
        return render_template('signin.html')
    flash('Your account has been created!', 'success')
    return render_template('signup.html')


@app.route('/add_post',methods=['GET','POST'])
@login_required
def add_post():
    user = User.query.all()
    if request.method == 'POST':
        alphabet = string.ascii_letters + string.digits
        post_key = ''.join(secrets.choice(alphabet) for i in range(32))
        title = request.form['title']
        body = request.form.get('ckeditor')
        post = Post(title=title,body=body,post_key=post_key,user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('addpost.html')



@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user:
            if check_password_hash(user.password_hash, request.form['password']):
                login_user(user, remember=True)
            return redirect(url_for('home'))
        flash('invalid Username or Password')
        return redirect(url_for('login'))
    return render_template('signin.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')



@app.route('/view_post/<post_key>')
@login_required
def view_post(post_key):
    post = Post.query.get(post_key)
    return render_template('post.html', post=post)


@app.route('/auth_profile/<int:id>')
def auth_profile(id):
    author = User.query.get(id)
    return render_template('author_profile.html', author=author)

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
