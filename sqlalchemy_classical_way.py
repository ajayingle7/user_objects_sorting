from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,Float
from sqlalchemy.orm import sessionmaker,mapper

#URL CREATE OF DATABASE
DB_URL = 'mysql://root:1234@localhost:3306/pdbc'

#CREATE OBJECT OF create_engine class
ENG = create_engine(DB_URL)


class Employee():
    def __init__(self,eid,n,sal,c):
        self.eid = eid
        self.name = n
        self.salary = sal
        self.city = c

    def __str__(self):
        return f"ID: {self.eid}, NAME:{self.name}, SALARY:{self.salary},CITY:{self.city}"


md = MetaData()

tb = Table('employee_info',md,
           Column('eid',Integer,primary_key=True),
           Column('name',String(50)),
           Column('salary',Float),
           Column('city',String(50))
           )
mapper(Employee,tb)

md.create_all(ENG)
Session = sessionmaker(bind=ENG)
sess = Session()

e1  =Employee(1,'Ajay',79888.4,'Pune')
e2  = Employee(2,'Vipul',478855.4,'Mumbai')
e3 = Employee(3,'Vijay',74955.25,'Satara')
e4 = Employee(4,'Sachin',58744.1,'Kaij')

sess.add_all([e1,e2,e3,e4])

result = sess.query(Employee)

for i in result:
    print(i)
sess.commit()

