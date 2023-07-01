import pytest
from myapp import create_app, create_test_app, db
from models import Book
from app import app


def test_request_example():
    app.config.update({
        "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db",
    })
    client = app.test_client()
    # with app.app_context():
    #     db.create_all()
    #     book1 = Book(id=2, author="foo", language="bar", title="test")
    #     db.session.add(book1)
    #     db.session.commit()
    
    response = client.get("/books")
    #print(response.json())
    assert response.status_code == 200

# def test_request_example():
#     client = app.test_client()
#     # with app.app_context():
#     #     db.create_all()
#     #     book1 = Book(id=2, author="foo", language="bar", title="test")
#     #     db.session.add(book1)
#     #     db.session.commit()
    
#     response = client.get("/books")
#     #print(response.json())
#     assert response.status_code == 200

    

# def test_request_example():
#     app = create_test_app()
#     client = app.test_client()
#     with app.app_context():
#         db.create_all()
#         book1 = Book(id=4, author="foo", language="bar", title="test")
#         db.session.add(book1)
#         db.session.commit()
    
#     response = client.get("/books")
#     #print(response.json())
#     assert response.status_code == 200





def test_post_api_endpoint():
    #with app.test_client() as c:
    app.config.update({
        "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db",
    })
    client = app.test_client()
    response = client.post('/books', data={
        "author": "J. K. Rowling",
        "language": "English",
        "title": "Unit Testing",
    })
    assert response.content_type == 'text/html; charset=utf-8'
    assert response.status_code == 201
    text_response = response.get_data(as_text=True)
    assert text_response == 'Book created successfully'



# def test_request_example(app_with_db):
#     response = app_with_db.get("/books")
#     #print(response.json())
#     assert response.status_code == 200
#     #assert response.content_type == 'application/json'

# def test_get_api_endpoint():
#     with app.test_client() as c:
#         response = c.get('/books')
#         assert response.status_code == 200
#         assert response.content_type == 'application/json'

# # #TODO: not alter production DB
# def test_post_api_endpoint():
#     with app.test_client() as c:
#         response = c.post('/books', data={
#             "author": "J. K. Rowling",
#             "language": "English",
#             "title": "Unit Testing",
#         })
#         assert response.content_type == 'text/html; charset=utf-8'
#         assert response.status_code == 201
#         text_response = response.get_data(as_text=True)
#         assert text_response == 'Book created successfully'

# def test_post_api_endpoint(db_session):
#     with app.test_client() as c:
#         response = c.post('/books', data={
#             "author": "J. K. Rowling",
#             "language": "English",
#             "title": "Unit Testing",
#         })
#         assert response.content_type == 'text/html; charset=utf-8'
#         assert response.status_code == 201
#         text_response = response.get_data(as_text=True)
#         assert text_response == 'Book created successfully'


#Future enhancement: test the individual book get, put, delete

# def test_post_api_endpoint():
#     with app.test_client() as c:
#         with app.app_context():
#             # Set up the transaction so that the post request will not alter the actual DB
#             connection = app.extensions['sqlalchemy'].db.engine.connect()
#             transaction = connection.begin()
            
#             # Make sure the session is bound to the connection
#             app.extensions['sqlalchemy'].db.session.configure(bind=connection)

#             # Perform your test actions here, such as sending a POST request
#             # to your API endpoint and asserting the expected response
#             response = c.post('/books', data={
#                 "author": "J. K. Rowling",
#                 "language": "English",
#                 "title": "Unit Testing New",
#             })
#             assert response.content_type == 'text/html; charset=utf-8'
#             assert response.status_code == 201
#             text_response = response.get_data(as_text=True)
#             assert text_response == 'Book created successfully'
            
#             # Roll back the transaction
#             transaction.rollback()
#             connection.close()

#Future enhancement: test the individual book get, put, delete