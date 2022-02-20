from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import author, favorite, book

@app.route('/')
def index():
  return render_template('index.html', authors=author.Author.get_all())

@app.route('/authors/create', methods=['POST'])
def authors_create():
  author.Author.create(request.form)
  return redirect('/')

@app.route('/authors/<int:author_id>')
def author_view(author_id):
  return render_template('/author.html', author=author.Author.get_one_with_books({'id' : author_id}), books=book.Book.get_unfavs({'author_id': author_id}))

@app.route('/favorites/create', methods=['POST'])
def favorites_create():
  favorite.Favorite.create(request.form)
  return redirect(f'/authors/{request.form["author_id"]}')