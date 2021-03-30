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
print(type(insert_stmt)) #<class 'sqlalchemy.sql.expression.Insert'>
print(insert_stmt) #INSERT INTO authors (id, name) VALUES (:id, :name)

compiled_stmt = insert_stmt.compile() #tried to add an empty object
print(compiled_stmt.params) #{'id': None, 'name': None}

# insert_stmt.execute(name='Alexandre Dumas') # insert a single entry
# insert_stmt.execute([{'name': 'Mr X'}, {'name': 'Mr Y'}]) # a list of entries
# metadata.bind = engine # no need to explicitly bind the engine from now on
# select_stmt = authors_table.select(authors_table.c.id==2)
# result = select_stmt.execute()
# result.fetchall() #[(1, u'Mr X')]
# del_stmt = authors_table.delete()
# del_stmt.execute(whereclause=text("name='Mr Y'"))
# del_stmt.execute() # delete all
