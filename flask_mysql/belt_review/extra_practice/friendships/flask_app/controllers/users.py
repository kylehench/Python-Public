from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user

@app.route('/')
def index():
  return render_template('index.html', users=user.User.get_all(), friendships=user.User.get_all_with_friends())

@app.route('/users/create', methods=['POST'])
def users_create():
  user.User.create(request.form)
  return redirect('/')