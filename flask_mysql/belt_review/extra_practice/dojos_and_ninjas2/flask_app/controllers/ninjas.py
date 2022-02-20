from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import ninja, dojo

@app.route('/ninjas/new')
def ninjas_new():
  return render_template('ninjas-new.html', dojos=dojo.Dojo.get_all())

@app.route('/ninjas/create', methods=['POST'])
def ninjas_create():
  ninja.Ninja.create(request.form)
  return redirect('/')