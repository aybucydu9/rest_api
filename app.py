import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from flask_session import Session
import json
import pymysql

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DB_conn']

db = SQLAlchemy(app)

# Create Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(200), nullable=False)
    language = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(200), nullable=False)

@app.route('/books', methods = ['GET', 'POST'])
def books():

    if request.method == 'GET':
        res = Book.query.all()

        books = [
            dict(id=row.id, author=row.author, language=row.language, title=row.title)
            for row in res
        ]
        if books is not None:
            return jsonify(books)

    if request.method == 'POST':
        data = request.form
        new_author = data.get('author')
        new_lang = data.get('language')
        new_title = data.get('title')
        
        new_book = Book(author=new_author,
                        language=new_lang,
                        title=new_title)
        db.session.add(new_book)
        db.session.commit()

        return "Book created successfully", 201
    
@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    book = None
    if request.method == 'GET':
        rows = Book.query.filter(Book.id == id).all()

        for r in rows:
            book = r
        if book is not None:
            book_json = {
            "id": book.id,
            "author": book.author,
            "language": book.language,
            "title": book.title 
            }        
            return jsonify(book_json), 200
        else:
            return "Something wrong", 404
        
    if request.method == 'PUT': 
        author = request.form['author']
        language = request.form['language']
        title = request.form['title']

        book_to_update = Book.query.get_or_404(id)
        book_to_update.author = author
        book_to_update.language = language
        book_to_update.title = title

        db.session.commit()

        updated_book = {
            "id": id,
            "author": author,
            "language": language,
            "title": title 
        }        

        return jsonify(updated_book)
    
    if request.method == 'DELETE':
       query = Book.query.filter_by(id=id).first()
       db.session.delete(query)
       db.session.commit()
       
       return "The book with id: {} has been deleted.".format(id), 200


if __name__== '__main__':
    app.run()