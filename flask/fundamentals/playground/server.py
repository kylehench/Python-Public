from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play/')
def hello_world1():
    return render_template('index.html', integer=3, color='lightblue')

@app.route('/play/<string_int>')
def hello_world2(string_int):
    return render_template('index.html', integer=int(string_int), color='lightblue')

@app.route('/play/<string_int>/<color>')
def hello_world3(string_int, color):
    return render_template('index.html', integer=int(string_int), color=color)

if __name__ == '__main__':
    app.run(debug=True)