import MySQLdb

mydb = MySQLdb.Connect(
    host = 'localhost',
    user= 'root',
    password = '1234',
    db =  'pdbc'


)
print(mydb)
print(type(mydb))


mycusor = mydb.cursor()

mycusor.execute('select * from laptop;')

for i in mycusor:
    print(i)

mydb.commit()
mydb.close()