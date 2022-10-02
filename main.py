import sqlalchemy
from sqlalchemy.orm import sessionmaker
from test import create_tables, Publisher, Book, Stock, Shop, Sale

DSN = 'postgresql://postgres:89242565295M@localhost:5432/database_test6'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)


Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name="PiderSHouse", id=1)
book1 = Book(id=1, title="Operachiaimir", publisher=publisher1)
shop1 = Shop(name="BalandaShop", id=1)
stock1 = Stock(count=10, book=book1, id=1, shop=shop1)
sale1 = Sale(id=1, count=5, price=1000, stock=stock1, data_sale="25.09.21")
session.add_all([publisher1, book1, stock1, sale1, shop1])
#
session.commit()
# print(book1.id)

def search_publisher():
    publisher_data = input("Введите id или имя ")
    if publisher_data.isdigit() == True:
        for data in session.query(Publisher).filter(Publisher.id == publisher_data):
            return print(data.id, data.name)
    else:
        for data in session.query(Publisher).filter(Publisher.name == publisher_data):
            return print(data.id, data.name)

search_publisher()


session.close()
