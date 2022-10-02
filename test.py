import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
#DSN = 'postgresql://postgres:89242565295M@localhost:5432/database_test6'
#engine = sqlalchemy.create_engine(DSN)

#Session = sessionmaker(bind=engine)
#session = Session()
#session.close()

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=56), unique=True)
    def __str__(self):
        return f'{self.id}:{self.name}'

class Book(Base):
    __tablename__ = "book"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String(length=56), unique=True)
    id_publisher = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("publisher.id"), nullable=False)
    publisher = relationship(Publisher, backref="book")
    def __str__(self):
        return f'{self.id}:{self.title},{self.id_publisher}'

class Shop(Base):
    __tablename__ = "shop"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=56), unique=True)
    def __str__(self):
        return f'{self.id}:{self.name}'

class Stock(Base):
    __tablename__ = "stock"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    count = sqlalchemy.Column(sqlalchemy.Integer)
    id_book = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("book.id"), nullable=False)
    id_shop = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("shop.id"), nullable=False)
    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")
    def __str__(self):
        return f'{self.id}:{self.count}'


class Sale(Base):
    __tablename__ = "sale"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    count = sqlalchemy.Column(sqlalchemy.String(length=56), unique=True)
    price = sqlalchemy.Column(sqlalchemy.Integer)
    data_sale = sqlalchemy.Column(sqlalchemy.String)
    id_stock = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("stock.id"), nullable=False)
    stock = relationship(Stock, backref="sale")
    def __str__(self):
        return f'{self.id}:{self.count},{self.price},{self.stock},{self.data_sale}'


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)