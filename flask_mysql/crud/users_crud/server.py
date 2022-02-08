from flask import Flask, render_template, session, redirect, request
from user import User
app = Flask(__name__)
app.secret_key = 'jkgnwjvndk048204823#*$)@'

@app.route('/')
def index():
  return redirect('/users')

@app.route('/users')
def users():
  users = User.get_all()
  return render_template('/users.html', users=users)

@app.route('/users/new')
def new_user():
  return render_template('/new_user.html')

@app.route('/process', methods=['POST'])
def process():
  data = {
    "first_name" : request.form['first_name'],
    "last_name" : request.form['last_name'],
    "email" : request.form['email']
  }
  User.save(data)
  return redirect('/users')

if __name__=='__main__':
  app.run(debug=True)