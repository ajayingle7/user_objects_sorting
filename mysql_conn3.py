import MySQLdb

conn = MySQLdb.Connect(
    host='localhost',
    user='root',
    password='1234',
    db='pdbc'
)

mycursor = conn.cursor()

while True:
    print("--- CHOOSE OPTIONS --\n"
          "1. CREATE TABLE\n"
          "2. INSERT RECORD\n"
          "3. UPDATE RECORD \n"
          "4. DELETE RECORD \n"
          "5. SHOW DATA \n"
          "6. SHOW CURRENT DATABASE\n"
          "7. QUIT")

    ch = int(input("enter a choice: "))

    if ch == 1:
        tbl_name = input("enter a table name: ")

        mycursor.execute(f'create table {tbl_name} (laptop_id int, brand varchar(255), price int);')

    elif ch == 2:
        tbl_name = input("enter a table name: ")
        records = int(input("how many records you want to add ?: "))

        for i in range(records):
            laptop_id = int(input("enter laptop_id : "))
            brand = input("enter brand: ")
            price = int(input("enter price: "))
            mycursor.execute(f'insert into {tbl_name} values ({laptop_id},"{brand}",{price})')


    elif ch == 3:
        tbl_name = input("enter a table name: ")
        print("--what do you want to update--\n"
              "1. laptop_id \n"
              "2. brand \n"
              "3. price")

        ch1 = int(input("enter a choice: "))

        if ch1 == 1:
            laptop_id = int(input("enter new laptop_id: "))
            brand = input("enter reference brand: ")
            mycursor.execute(f'update {tbl_name} set laptop_id={laptop_id} where brand ="{brand}";')

        elif ch1 == 2:
            brand = (input("enter new brand: "))
            laptop_id = int(input("enter reference laptop_id: "))
            mycursor.execute(f'update {tbl_name} set brand = "{brand}" where laptop_id ={laptop_id};')

        elif ch1 == 3:
            price = int(input("enter new price: "))
            laptop_id = int(input("enter reference laptop_id: "))
            mycursor.execute(f'update {tbl_name} set price= {price} where laptop_id ={laptop_id};')

    elif ch == 4:
        tbl_name = input("enter a table name: ")
        laptop_id = int(input("enter a laptop_id: "))

        mycursor.execute(f"delete from {tbl_name} where laptop_id = {laptop_id};")


    elif ch == 5:
        tbl_name = input("enter a table name: ")
        mycursor.execute(f'select * from {tbl_name};')

        for i in mycursor:
            print(i)


    elif ch == 6:
        mycursor.execute('select database()')
        for i in mycursor:
            print(i)


    elif ch == 7:
        break

    else:
        print('enter right choice')

    conn.commit()
    conn.close()





