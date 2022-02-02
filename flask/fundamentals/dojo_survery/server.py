from distutils.log import debug
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'jlujknohkjmjlnkdfwcsrsdsacsfdfxd54525488793948539'

loc_dict = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-survey', methods=['POST'])
def process():
    session['name'] = request.form['name']
    print(session)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')
    
if __name__=='__main__':
    app.run(debug=True)