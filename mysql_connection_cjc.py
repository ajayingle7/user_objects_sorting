import MySQLdb

conn = MySQLdb.connect(
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
          "5. SELECT DATA\n"
          "6. SHOW CURRENT DATABASE\n"
          "7. ALTER TABLE\n"
          "8. DESCRIBE TABLE\n"
          "9. DROP TABLE\n"
          "10. QUIT\n"
          )

    ch = int(input("enter a choice: "))

    if ch == 1:
        tbl_name = input("enter a table name: ")

        mycursor.execute(f'create table {tbl_name} (rn int, name varchar(255), marks int);')

    elif ch == 2:
        tbl_name = input("enter a table name: ")
        records = int(input("how many records you want to add ?: "))

        for i in range(records):
            rn = int(input("enter roll no: "))
            name = input("enter name: ")
            marks = int(input("enter marks: "))
            mycursor.execute(f'insert into {tbl_name} values ({rn},"{name}",{marks})')

            print("QUERY EXECUTED SUCCESSFULY.....")


    elif ch == 3:
        tbl_name = input("enter a table name: ")
        print("--what do you want to update--\n"
              "1. roll \n"
              "2. name \n"
              "3. marks")

        ch1 = int(input("enter a choice: "))

        if ch1 == 1:
            roll = int(input("enter new rno: "))
            name = input("enter reference name: ")
            mycursor.execute(f'update {tbl_name} set rn={roll} where name1 ="{name}"')
            print("QUERY EXECUTED SUCCESSFULY.....")

        elif ch1 == 2:
            name = (input("enter new name: "))
            rno = int(input("enter reference rno: "))
            mycursor.execute(f'update {tbl_name} set name1 = "{name}" where rn ={rno};')
            print("QUERY EXECUTED SUCCESSFULY.....")

        elif ch1 == 3:
            marks = int(input("enter new marks: "))
            rno = int(input("enter reference rno: "))
            mycursor.execute(f'update {tbl_name} set marks = {marks} where rn ={rno}')
            print("QUERY EXECUTED SUCCESSFULY.....")

    elif ch == 4:
        tbl_name = input("enter a table name: ")
        rn = int(input("enter a reference rno: "))

        mycursor.execute(f"delete from {tbl_name} where rn= {rn}")
        print("QUERY EXECUTED SUCCESSFULY.....")


    elif ch == 5:
        tbl_name = input("enter a table name: ")
        mycursor.execute(f'select * from {tbl_name};')

        for i in mycursor:
            print(i)

        print("QUERY EXECUTED SUCCESSFULY.....")


    elif ch == 6:
        mycursor.execute('select database()')
        for i in mycursor:
            print(i)
        print("QUERY EXECUTED SUCCESSFULY.....")


    elif ch == 7:
        tbl_name = input('enter a table name: ')
        print("--what do you want to alter ? "
              "1. change data type\n"
              "2. change table name\n"
              "3. change column name\n"
              "4. add new column\n"
              "5. drop column"
              )
        ch2 = int(input("enter a choice: "))

        if ch2==1:
            name = input("enter a column name: ")
            datatype = input("enter new datatype: ")

            mycursor.execute(f'alter table {tbl_name} modify {name} {datatype};')
            print("QUERY EXECUTED SUCCESSFULY.....")

        elif ch2==2:
            new_tbl_name = input("enter a new table name: ")

            mycursor.execute(f'alter table {tbl_name} rename to {new_tbl_name};')
            print("QUERY EXECUTED SUCCESSFULY.....")


        elif ch2==3:
            column = input("enter which column you want to change: ")
            new_column = input("which name want to set for new column: ")
            datatypee = str(input("enter datatype for that column: "))


            mycursor.execute(f'alter table {tbl_name} change column {column} {new_column} {datatypee};')
            print("QUERY EXECUTED SUCCESSFULY.....")

        elif ch2 ==4:
            new_column = input("enter new column name: ")
            datatypeee = str(input("enter datatype for new column: "))


            mycursor.execute(f"alter table {tbl_name} add {new_column} {datatypeee};")
            print("QUERY EXECUTED SUCCESSFULY.....")

        elif ch2==5:

            column_name = input("enter a column name of which do you want to drop: ")
            mycursor.execute(f'alter table {tbl_name} drop column {column_name};')
            print("QUERY EXECUTED SUCCESSFULY.....")


    elif ch==8:
        mycursor.execute('show tables;')
        for i in mycursor:
            print(i)


        tbl_name = input("enter table name from above tables : ")
        mycursor.execute(f'desc {tbl_name};')
        for i in mycursor:
            print(i)
        print("QUERY EXECUTED SUCCESSFULY.....")

    elif ch==9:
        tbl_name  = input("enter table name which you want to drop: ")

        mycursor.execute(f'drop table {tbl_name};')
        for i in mycursor:
            print(i)


    elif ch==10:
        break

    else:
        print('please enter right choice')

    conn.commit()
    conn.close()










