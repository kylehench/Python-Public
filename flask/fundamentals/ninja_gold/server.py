from random import randint
import datetime
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'jkgnwjvndk048204823#*$)@'

places = {'Farm':{'description':'earns 10-20 golds', 'earns':[10,20]},
    'Cave':{'description':'earns 5-10 golds', 'earns':[5,10]},
    'House':{'description':'earns 2-5 golds', 'earns':[2,5]},
    'Casino':{'description':'earns/takes 0-50 golds', 'earns':[-50,50]}}

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'info' not in session:
        session['info'] = ''
    if 'info' not in session:
        session['info'] = ''
    return render_template('index.html', gold=session['gold'], places=places, info=session['info'])

@app.route('/process_money', methods=['post'])
def process_money():
    now = datetime.datetime.now()
    now_str = now.strftime('%Y-%m-%d %I:%M:%S %p')
    list1 = places[request.form['place']]['earns']
    gold_change = randint(list1[0],list1[1])
    session['gold'] += gold_change
    if request.form['place'] == 'Casino':
        next_msg = 'Entered a casino and '
        if gold_change >= 0:
            next_msg += f'gained {gold_change} golds... Nice! ({now_str})'
        else:
            next_msg += f'lost {gold_change} golds... Ouch... ({now_str})'
    else:
        next_msg = f"Earned {gold_change} golds from the {request.form['place'].lower()} ({now_str})"
    if gold_change >= 0:
        session['info'] = f'<li class="text-success">{next_msg}</li>' + session['info']
    else:
        session['info'] = f'<li class="text-danger">{next_msg}</li>' + session['info']
    return redirect('/')

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)