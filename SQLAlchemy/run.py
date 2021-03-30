# https://docs.sqlalchemy.org/en/14/core/tutorial.html
# Using the Table objects directly
# We don't even need to map our Table-objects in order to manipulate our tables


from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text

engine = create_engine('sqlite:///library.db', echo=True) # create an Engine object # connection to the database

metadata = MetaData()

authors_table = Table('authors',   # define and create tables
                    metadata,
                    Column('id', Integer, primary_key=True), 
                    Column('name', String))

books_table = Table('books', 
                    metadata,
                    Column('id', Integer, primary_key=True),
                    Column('title', String),
                    Column('description', String),
                    Column('author_id', ForeignKey('authors.id')))
# Column('name', String(50)) is possible
metadata.create_all(engine)   # define and create tables

# Using the Table objects directly
# We don't even need to map our Table-objects in order to manipulate our tables

insert_stmt = authors_table.insert(bind=engine) #engine може бути кілька різних, тому я вказую, якої саме бази даних стосуватиметься команда insert
print(type(insert_stmt)) #<class 'sqlalchemy.sql.expression.Insert'>
print(insert_stmt) #INSERT INTO authors (id, name) VALUES (:id, :name)

compiled_stmt = insert_stmt.compile() #tried to add an empty object
print(compiled_stmt.params) #{'id': None, 'name': None}

insert_stmt.execute(name='Alexandre Dumas') # insert a single entry
insert_stmt.execute([{'name': 'Mr X'}, {'name': 'Mr Y'}]) # a list of entries

metadata.bind = engine # no need to explicitly bind the engine from now on # можемо напряму працювати з об'єктами

select_stmt = authors_table.select(authors_table.c.id==2) # будуємо sql-запит
result = select_stmt.execute()
# print("result start")
# print(result)
# print("result end")

result.fetchall() #[(1, u'Mr X')] # A synonym for the Result.all() method.
# These methods return row objects, which are provided via the Row class. The result object can be iterated directly in order to provide an iterator of Row objects:

del_stmt = authors_table.delete(whereclause=text("name='Mr Y'"))
# del_stmt.execute(whereclause=text("name='Mr Y'"))
del_stmt.execute()



##################################
# Classical mapping. Now we can define our classes and create a mapping

from sqlalchemy.orm import mapper, relation, backref
# from sqlalchemy.orm import relationship, backref


class Author:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class Book:
    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author
    def __repr__(self):
        return self.title
