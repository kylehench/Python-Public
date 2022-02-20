from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import dojo

@app.route('/')
def index():
  return redirect('/dojos')

@app.route('/dojos')
def dojos():
  return render_template('index.html', dojos=dojo.Dojo.get_all())

@app.route('/dojos/create', methods=['POST'])
def dojos_create():
  dojo.Dojo.create(request.form)
  return redirect('/')
  
@app.route('/dojos/<int:id>')
def view_dojo(id):
  return render_template('dojo.html', dojo=dojo.Dojo.get_one_with_ninjas({'id' : id}))