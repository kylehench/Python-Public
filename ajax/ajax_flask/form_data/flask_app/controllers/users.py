from flask_app.models.user import User
from flask_app import app
from flask_app.models import user
from flask import render_template, jsonify, request, redirect

@app.route('/')
def index():
    return render_template('index.html', users = user.User.get_all_json())

@app.route('/users')
def users():
    return jsonify(User.get_all_json())

@app.route('/create/user', methods=['POST'])
def create_user():
    user.User.save(request.form)
    return jsonify(message="Add a user!!!")