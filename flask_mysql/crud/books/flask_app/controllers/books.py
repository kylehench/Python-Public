from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import book
from flask_app.models import author

@app.route('/books')
def show_books():
  books = book.Book.get_all()
  return render_template('books.html', books=books)

@app.route('/process/new-book', methods=['POST'])
def new_book():
  data = {
    'title' : request.form['title'],
    'num_of_pages' : request.form['num_of_pages']
  }
  book.Book.add_book(data)
  return redirect('/books')

@app.route('/books/<id>')
def show_book(id):
  print('show book > var "id":  ',id)
  one_book = book.Book.get_one_with_authors({'id' : id})
  return render_template('book.html', one_book=one_book, all_authors = author.Author.unfav_authors({'id' : id}))