from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import ninja
from flask_app.models import dojo

@app.route('/ninjas')
def ninjas():
  return render_template('add_ninja.html', dojos = dojo.Dojo.get_all())

@app.route('/process/add_ninja', methods=['POST'])
def process_ninja():
  data = {
    'dojo_id' : request.form['dojo_id'],
    'first_name' : request.form['first_name'],
    'last_name' : request.form['last_name'],
    'age' : request.form['age'],
  }
  print(data)
  ninja.Ninja.save(data)
  return redirect('/dojos')