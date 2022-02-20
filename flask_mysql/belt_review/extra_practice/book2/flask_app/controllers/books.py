from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import book, author, favorite

@app.route('/books')
def books():
  return render_template('books.html', books=book.Book.get_all())

@app.route('/books/<int:id>')
def book_view(id):
  return render_template('book.html', book=book.Book.get_one_with_authors({'id':id}), authors=author.Author.get_unfavs({'book_id': id}))
  
@app.route('/books/create', methods=['POST'])
def books_create():
  book.Book.create(request.form)
  return redirect('/books')

@app.route('/favorites/create/return_book', methods=['POST'])
def favorites_create_return_book():
  favorite.Favorite.create(request.form)
  return redirect(f'/books/{request.form["book_id"]}')