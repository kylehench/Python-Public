from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = '048584039485034950393848950922849484840193939105848720940393849292839405959599991938495893810948293944493012939'

@app.route('/')
def index():
    if 'click_count' in session:
        session['click_count'] += 1
    else:
        session['click_count'] = 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)