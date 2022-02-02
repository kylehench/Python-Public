from distutils.log import debug
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'jlujknohkjmjlnkdfwcsrsdsacsfdfxd54525488793948539'

loc_list = ['Online', 'Bellevue', 'Burbank', 'Chicago', 'San Jose', 'Seattle']

lang_list = ['HTML', 'CSS', 'JavaScript', 'Python', 'Java']

form_list = ['Name', 'Location', 'Language','Pacing', 'Comments']

pacing_list = ['Just right', 'A little fast', 'A little slow']

@app.route('/')
def index():
    return render_template('index.html', loc_list=loc_list, lang_list=lang_list, pacing_list=pacing_list)

@app.route('/process-survey', methods=['post'])
def process():
    for value in form_list:
        if value in request.form:
            session[value] = request.form[value]
        else:
            session[value] = 'null'
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', form_list=form_list)
    
if __name__=='__main__':
    app.run(debug=True)