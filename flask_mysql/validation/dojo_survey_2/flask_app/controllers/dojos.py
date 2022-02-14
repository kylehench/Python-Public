from flask_app import app
from flask import Flask, render_template, request, redirect, session
from flask_app.models import dojo

loc_list = ['Online', 'Bellevue', 'Burbank', 'Chicago', 'San Jose', 'Seattle']
lang_list = ['HTML', 'CSS', 'JavaScript', 'Python', 'Java']
form_list = ['Name', 'Location', 'Language','Pacing', 'Comment']
pacing_list = ['Just right', 'A little fast', 'A little slow']

@app.route('/')
def index():
    return render_template('index.html', loc_list=loc_list, lang_list=lang_list, pacing_list=pacing_list)

@app.route('/process-survey', methods=['post'])
def process():
    print(request.form)
    if not dojo.Dojo.validate_dojo(request.form):
        return redirect('/')
    for value in form_list:
        if value.lower() in request.form:
            session[value] = request.form[value.lower()]
        else:
            session[value] = 'null'
    print(dojo.Dojo.create(request.form))
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', form_list=form_list)