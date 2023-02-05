from flask import Flask, request  # Import Flask to allow us to create our app
from flask_cors import CORS, cross_origin
import jwt, os
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
cors = CORS(app, headers=['Content-Type'], expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True)
# app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY']=os.environ.get("SECRET_KEY")

@app.route('/')          # The "@" decorator associates this route with the function immediately following
@cross_origin()
def hello():
    token = None
    if 'x-access-tokens' in request.headers:
        token = request.headers['x-access-tokens']
        print('token found!')
    else:
        print('token missing :(')

    if not token:
        return 'a valid token is missing'
        
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        print('success')
        return 'success'
    except:
        print('token decode failed')
        return 'token decode failed'


@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry! No response. Try again.'
    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=8000)    # Run the app in debug mode.