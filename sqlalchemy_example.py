from sqlalchemy import create_engine, Table, MetaData, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, mapper

DB_URL = 'mysql://root:1234@localhost:3306/pdbc'

ENG = create_engine(DB_URL)


class Laptop():
    def __init__(self, laptop_id, brand, price):
        self.laptop_id = laptop_id
        self.brand = brand
        self.price = price

    def __str__(self):
        return f'Laptop_Id: {self.laptop_id}, Name: {self.brand}, Price: {self.price}'


md = MetaData()

tb = Table('laptop', md,
           Column('laptop_id', Integer, primary_key=True),
           Column('brand', String(10)),
           Column('price', Integer))

mapper(Laptop, tb)

md.create_all(ENG)

Session = sessionmaker(bind=ENG)

sess = Session()

while True:

    print("--CHOOSE OPTIONS--\n"
          "1.CREATE TABLE\n"
          "2.UPDATE TABLE\n"
          "3.DELETE TABLE\n"
          "4.RETEIVE DATA")

    ch = int(input("enter chice: "))

    if ch == 1:

        objects = int(input("enter how many records: "))

        list1 = []

        for i in range(objects):
            laptop_id = int(input("enter laptop_id: "))
            brand = input("enter brand name: ")
            price = int(input("enter price: "))

            obj1 = Laptop(laptop_id, brand, price)

            list1.append(obj1)

            sess.add_all(list1)
            sess.commit()


    elif ch == 2:

        print("--what do you want to update--\n"
              "1.LAPTOP_ID\n"
              "2.BRAND\n"
              "3.PRICE")

        ch2 = int(input("enter a choice"))

        if ch2 == 1:
            brand = input("enter ref brand: ")
            laptop_id = int(input("enter a new laptop_id"))

            sess.query(Laptop).filter(Laptop.brand == brand).update({Laptop.laptop_id: laptop_id})
            sess.commit()


        elif ch2 == 2:

            laptop_id = int(input('enter ref laptop_id'))
            brand = input('enter a new brand name: ')

            sess.query(Laptop).filter(Laptop.laptop_id == laptop_id).update({Laptop.brand: brand})
            sess.commit()


        elif ch2 == 3:

            price = int(input("enter a new price: "))
            laptop_id = int(input("enter a ref laptop_id: "))

            sess.query(Laptop).filter(Laptop.laptop_id == laptop_id).update({Laptop.price: price})
            sess.commit()

    elif ch == 3:
        laptop_id = int(input("enter laptop_id: "))

        sess.query(Laptop).filter(Laptop.laptop_id == laptop_id).delete()
        sess.commit()


    elif ch == 4:

        result = sess.query(Laptop)

        for i in result:
            print(i)

        sess.commit()


    elif ch == 5:
        break

    else:
        print('choose right option')







































































