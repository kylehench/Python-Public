from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'hello, world'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string>')
def say(string):
    if isinstance(string, str):
        return f'Hi {string[0].upper()}{string[1:]}!'

@app.route('/repeat/<string_int>/<string>')
def repeat(string_int, string):
    if not isinstance(string_int, str) or \
        not isinstance(string, str) or \
        not string_int.isdigit():
        return ''
    output = ''
    for i in range(int(string_int)):
        output += f'<p>{string}</p>'
    return output

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry! No response. Try again.'
    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.