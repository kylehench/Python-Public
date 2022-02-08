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

@app.route('/users/<id>')
def show_user(id):
  user = User.get_id(id)[0]
  return render_template('/show_user.html', user=user)

@app.route('/users/<id>/edit')
def edit_user(id):
  user = User.get_id(id)[0]
  return render_template('/update_user.html', id=id, user=user)

@app.route('/process/users/<id>/edit', methods=['POST'])
def process_user_edit(id):
  data = {
    "first_name" : request.form['first_name'],
    "last_name" : request.form['last_name'],
    "email" : request.form['email'],
    "id" : id
  }
  User.update_id(data)
  return redirect(f'/users/{id}')

@app.route('/users/<id>/delete')
def delete_user(id):
  User.delete_id(id)
  return redirect('/users')

@app.route('/process', methods=['POST'])
def process():
  data = {
    "first_name" : request.form['first_name'],
    "last_name" : request.form['last_name'],
    "email" : request.form['email']
  }
  id = User.save(data)
  return redirect(f'/users/{id}')

if __name__=='__main__':
  app.run(debug=True)