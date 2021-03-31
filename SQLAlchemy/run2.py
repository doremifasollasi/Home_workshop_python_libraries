from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text

engine = create_engine('sqlite:///library2.db', echo=True) # create an Engine object # connection to the database

# Declarative mapping # Doing the same thing the easy way:
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship(Author, backref=backref('books', order_by=title))

    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self):
        return self.title

Base.metadata.create_all(engine) # create tables
