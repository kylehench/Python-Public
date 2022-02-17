from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import message
from flask_bcrypt import Bcrypt
import datetime
bcrypt = Bcrypt(app)

@app.route('/messages/create', methods = ['POST'])
def messages_create():
  if message.Message.validate_message(request.form):
    message.Message.create(request.form)
  return redirect('/login/success')

@app.route('/messages/delete/<id>')
def messages_delete(id):
  one_message = message.Message.get_one({'id' : id})
  if session['user_id']==one_message.recipient_id:
    message.Message.delete({'id' : id})
    return redirect('/login/success')
  return redirect('/logout')

@app.route('/test')
def test():
  one_message = message.Message.user_messages({'recipient_id' : session['user_id']})[0]
  # time_obj = datetime.strptime(str(one_message.created_at), '%Y-%m-%d %H:%M:%S')
  print('DAYS:  ', (datetime.datetime.now()-one_message.updated_at).seconds)
  return redirect('/login/success')
