from flask import Flask, request, jsonify, Response  # Import Flask to allow us to create our app
import jwt, os
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY']=os.environ.get("SECRET_KEY")

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello():
    token = None
    print(request.headers)
    if 'cookie' in request.headers:
        token = request.cookies.get('usertoken')
        print('token found!')
    else:
        print('token missing :(')

    if not token:
        return 'a valid token is missing'
        
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        print('success')
        print(data)
        return jsonify(data)
    except:
        print('token decode failed')
        return 'token decode failed'


@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry! No response. Try again.'
    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=8000)    # Run the app in debug mode.