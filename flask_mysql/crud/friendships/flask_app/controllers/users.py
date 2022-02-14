from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import user

@app.route('/')
def index():
  return redirect('/friendships')

@app.route('/friendships')
def friendships():
  return render_template('index.html', users=user.User.get_all(), friends=user.User.get_friends())

@app.route('/users/new', methods = ['POST'])
def users_new():
  user.User.create(request.form)
  return redirect('/')

@app.route('/friendships/create', methods = ['POST'])
def friendships_create():
  user.User.friendships_create(request.form)
  return redirect('/')