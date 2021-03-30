from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text

engine = create_engine('sqlite:///library.db', echo=True) #connection to the database

metadata = MetaData()

authors_table = Table('authors', 
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
metadata.create_all(engine)  

#######################################

insert_stmt = authors_table.insert(bind=engine) #engine може бути кілька різних, тому я вказую, якої саме бази даних стосуватиметься команда insert
type(insert_stmt) #<class 'sqlalchemy.sql.expression.Insert'>
print (insert_stmt) #INSERT INTO authors (id, name) VALUES (:id, :name)


