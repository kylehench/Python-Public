from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import email

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/emails/create', methods = ['POST'])
def emails_create():
  if not email.Email.validate_email(request.form):
    return redirect('/')
  session['new_id'] = email.Email.create(request.form)
  return redirect('/success')

@app.route('/success')
def success():
  one_email = email.Email.get_one({'id' : session['new_id']})
  if one_email is None:
    one_email = False
  return render_template('success.html', emails=email.Email.get_all(), email=one_email)

@app.route('/destroy/<int:id>')
def destroy_email(id):
  email.Email.destroy({'id': id})
  return redirect('/success')