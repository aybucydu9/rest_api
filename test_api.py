from app import app

def test_get_api_endpoint():
    with app.test_client() as c:
        response = c.get('/books')
        assert response.status_code == 200
        assert response.content_type == 'application/json'

# #TODO: not alter production DB
def test_post_api_endpoint():
    with app.test_client() as c:
        response = c.post('/books', data={
            "author": "J. K. Rowling",
            "language": "English",
            "title": "Unit Testing",
        })
        assert response.content_type == 'text/html; charset=utf-8'
        assert response.status_code == 201
        text_response = response.get_data(as_text=True)
        assert text_response == 'Book created successfully'

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