from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import friendship

@app.route('/friendships/create', methods=['POST'])
def friendships_create():
  if friendship.Friendship.check(request.form):
    return redirect('/')
  friendship.Friendship.create(request.form)
  return redirect('/')