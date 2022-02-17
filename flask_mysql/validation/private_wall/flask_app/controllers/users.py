from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user
from flask_app.models import message
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/users/create', methods=['POST'])
def users_create():
  data = {key:value for key, value in request.form.items()}
  if user.User.validate_user(data)==False or user.User.validate_email(data)==False:
    return redirect('/')
  data['password'] = bcrypt.generate_password_hash(data['password'])
  user_id = user.User.create(data)
  session['user_id'] = user_id
  session['full_name'] = f'{data["first_name"]} {data["last_name"]}'
  return redirect('/login/success')

@app.route('/login', methods=['POST'])
def login():
  # see if the username provided exists in the database
  data = { "email" : request.form["email"] }
  user_in_db = user.User.get_by_email(data)
  # user is not registered in the db
  if not user_in_db:
    flash("Invalid Email/Password")
    return redirect("/")
  if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
    # if we get False after checking the password
    flash("Invalid Email/Password")
    return redirect('/')
  # if the passwords matched, we set the user_id into session
  session['user_id'] = user_in_db.id
  session['first_name'] = user_in_db.first_name
  session['full_name'] = user_in_db.full_name()
  return redirect('/login/success')

@app.route('/login/success')
def login_success():
  print(session)
  if 'user_id' not in session.keys():
    return redirect('/')
  return render_template('login-success.html', users=user.User.get_all(), messages = message.Message.user_messages({'recipient_id' : session['user_id']}), msg_count = message.Message.message_count({'user_id' : session['user_id']}))

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')