from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', x=8, y=8, color1='blue', color2='gray')

@app.route('/<string_x>')
def home_with_x(string_x):
    return render_template('index.html', x=int(string_x), y=8, color1='blue', color2='gray')

@app.route('/<string_x>/<string_y>')
def home_with_xy(string_x, string_y):
    return render_template('index.html', x=int(string_x), y=int(string_y), color1='blue', color2='gray')

@app.route('/<string_x>/<string_y>/<color1>/<color2>')
def home_with_xy_colors(string_x, string_y, color1, color2):
    return render_template('index.html', x=int(string_x), y=int(string_y), color1=color1, color2=color2)


if __name__=='__main__':
    app.run(debug=True)
