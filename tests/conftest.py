import pytest
from myapp import create_app, db
from models import Book
from app_test import app, db

@pytest.fixture(scope="session")
def flask_app():
    app.config.update({
        "TESTING": True,
    })
    app.config.update({
        "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db",
    })
    app.app_context().push()
    client = app.test_client()
    ctx = app.test_request_context()
    ctx.push()

    # other setup can go here

    yield client

    #app.app_context().pop()
    ctx.pop()

    # clean up / reset resources here

@pytest.fixture(scope="session")
def app_with_db(flask_app):    
    db.create_all()
    book1 = Book(id=2, author="foo", language="bar", title="test")
    db.session.add(book1)
    db.session.commit()
    yield flask_app
    db.session.commit()
    db.drop_all()






# @pytest.fixture(scope="session")
# def app():
#     app = create_app()
#     # app.config.update({
#     #     "TESTING": True,
#     # })
#     # app.config['TESTING'] = True
#     # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
#     # app.config.update({
#     #     "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db",
#     # })
#     #app.app_context().push()
#     client = app.test_client()
#     # ctx = app.test_request_context()
#     # ctx.push()
#     app.app_context().push()

#     # other setup can go here

#     yield client

#     app.app_context().pop()

#     # clean up / reset resources here

# @pytest.fixture(scope="session")
# def app_with_db(app):    
#     db.create_all()
#     book1 = Book(id=1, author="foo", language="bar", title="test")
#     db.session.add(book1)
#     db.session.commit()
#     yield app
#     db.session.commit()
#     db.drop_all()
#     # return app.test_client()



# # @pytest.fixture()
# # def client(app):
# #     client = app.test_client()
# #     #with app.app_context():
# #     db.create_all()
# #     book1 = Book(id=1, author="foo", language="bar", title="test")
# #     db.session.add(book1)
# #     db.session.commit()
# #     yield client
# #     db.session.commit()
# #     db.drop_all()
# #     # return app.test_client()
