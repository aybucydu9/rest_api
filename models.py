from sqlalchemy import Integer, String
from myapp import db

# Create Model
class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(Integer, primary_key=True)
    author = db.Column(String(200), nullable=False)
    language = db.Column(String(200), nullable=False)
    title = db.Column(String(200), nullable=False)