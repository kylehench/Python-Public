from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo

@app.route('/')
def index():
  return redirect('/dojos')

@app.route('/dojos')
def dojos():
  return render_template('dojos.html', dojos = dojo.Dojo.get_all())

@app.route('/dojos/<id>')
def one_dojo(id):
  return render_template('dojo.html', dojo = dojo.Dojo.get_one_with_ninjas(id=id))


@app.route('/new_dojo', methods=['POST'])
def new_dojo():
  data = {
    'name' : request.form['name']
  }
  dojo.Dojo.create(data)
  return redirect('/dojos')