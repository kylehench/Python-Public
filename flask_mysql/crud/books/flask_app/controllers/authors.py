from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import author
from flask_app.models import book
from flask_app.models import favorite

@app.route('/')
def index():
  return redirect('/authors')

@app.route('/authors')
def show_authors():
  authors = author.Author.get_all()
  return render_template('authors.html', authors=authors)

@app.route('/authors/create', methods=['POST'])
def new_author():
  id = author.Author.create(request.form)
  # return redirect('/authors')
  return redirect(f'/authors/{id}')

@app.route('/authors/<id>')
def show_author(id):
  one_author = author.Author.get_one_with_books({'id':id})
  books = book.Book.unfav_books({'id':id})
  return render_template('author.html', one_author=one_author, books=books)

@app.route('/favorites/create', methods=['POST'])
def create_favorite():
  favorite.Favorite.create_fav(request.form)
  author_id = request.form['author_id']
  if 'redirect' in request.form and request.form['redirect']=='book':
    book_id = request.form['book_id']
    return redirect(f'/books/{book_id}')
  return redirect(f'/authors/{author_id}')