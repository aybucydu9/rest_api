from flask import Flask, request, jsonify
import json
import pymysql

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = pymysql.connect(host='sql9.freesqldatabase.com',
                                database='sql9625882',
                                user='sql9625882',
                                password='upYjSe6z46',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    except pymysql.error as e:
        print(e)
    return conn

@app.route('/books', methods = ['GET', 'POST'])
def books():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM book")
        books = [
            dict(id=row['id'], author=row['author'], language=row['language'], title=row['title'])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)

    if request.method == 'POST':
        #if request.is_json:
        #    data = request.json
        data = request.form
        new_author = data.get('author')
        new_lang = data.get('language')
        new_title = data.get('title')
        sql = """ INSERT INTO book (author, language, title)
                  VALUES (%s, %s, %s)"""

        cursor = cursor.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        return "Book created successfully", 201
    
@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book = None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM book WHERE id=%s", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book), 200
        else:
            return "Something wrong", 404
        
    if request.method == 'PUT': 
        sql = """UPDATE book 
                SET title=%s,
                    author=%s,
                    language=%s
                WHERE id=%s"""
        
        author = request.form['author']
        language = request.form['language']
        title = request.form['title']
        updated_book = {
            "id": id,
            "author": author,
            "language": language,
            "title": title 
        }        
        cursor.execute(sql, (author, language, title, id))
        conn.commit()
        return jsonify(updated_book)
    
    if request.method == 'DELETE':
       sql = """ DELETE FROM book WHERE id=%s """
       cursor.execute(sql, (id,))
       conn.commit()
       return "The book with id: {} has been deleted.".format(id), 200


if __name__== '__main__':
    app.run(debug=True)
#TODO: change debug mode back