from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
# Declarative mapping # Doing the same thing the easy way:
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


engine = create_engine('sqlite:///library2.db', echo=True) # create an Engine object # connection to the database
                                                            #Note that echo=True is also passed here, this tells the engine object to log all the SQL it executed to sys.stdout.
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
        return f"{self.id} {self.title}"

Base.metadata.create_all(engine) # create tables

##################################
# Creating instances
# У попередньому блоці ми створили суто саму базу даних,
# У наступному блоці - для виконання запитів ми використовуватимемо Session() - об'єкт через, який ми робитимемо транзакції
# Щоб створити Session(), потірбно з orm дістати sessionmaker

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine) # bound session # генеруємо сесію, команда - відай мені такий пулінг сесії на engine - наша БД
session = Session()

# створюємо об'єкти зі сторони Python
author_1 = Author('Richard Dawkins')
author_2 = Author('Matt Ridley')
book_1 = Book('The Red Queen', 'A popular science book', author_2)
book_2 = Book('The Selfish Gene', 'A popular science book', author_1)
book_3 = Book('The Blind Watchmaker', 'The theory of evolutio', author_1)

# на цьому етапі ми лише створюємо транзакцію - кілька запити на додавання
session.add(author_1)
session.add(author_2)
session.add(book_1)
session.add(book_2)
session.add(book_3)
# or simply session.add_all([author_1, author_2, book_1, book_2, book_3])

print(book_3)
session.commit()

# а ось вже тут commit() внисе ці транзакції до БД
# session.commit() # це як команда push в git # також ця команда повертає об'єктові id

book_3.description = 'The theory of evolution' # update the object
# book_3 in session # check whether the object is in the session
# True
print(book_3)
# book_3.id = 2 # не можна так робити, адже id поле автоінкриментне, тому його не вийде засетати
session.commit()
