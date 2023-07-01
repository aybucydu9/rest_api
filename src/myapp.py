import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# don't pass in the app object yet
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///production.db"
    # Dynamically bind SQLAlchemy to application
    db.init_app(app)
    app.app_context().push()
    return app

def create_test_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    # Dynamically bind SQLAlchemy to application
    db.init_app(app)
    app.app_context().push() # this does the binding
    return app

# # you can create another app context here, say for production
# def create_production_app():
#     app = Flask(__name__)
#     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DB_conn']
#     # Dynamically bind SQLAlchemy to application
#     db.init_app(app)
#     app.app_context().push()
#     return app