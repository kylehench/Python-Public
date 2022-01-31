from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

# This is the last time we will have post method and render template in the same method

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    info = request.form
    fruits_count = int(info["apple"])+int(info["strawberry"])+int(info["raspberry"])
    print(fruits_count)
    print(f'Charging {info["first_name"]} {info["last_name"]} for {fruits_count} fruits')
    return render_template("checkout.html", info = info)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    