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
          "5. SHOW DATA \n"
          "6. SHOW CURRENT DATABASE\n"
          "7. QUIT")

    ch = int(input("enter a choice: "))

    if ch == 1:
        tbl_name = input("enter a table name: ")

        mycursor.execute(f'create table {tbl_name} (emp_id int, emp_name varchar(255), salary int);')

    elif ch == 2:
        tbl_name = input("enter a table name: ")
        records = int(input("how many records you want to add ?: "))

        for i in range(records):
            emp_id = int(input("enter emp_id : "))
            emp_name = input("enter emp_name: ")
            salary = int(input("enter salary: "))
            mycursor.execute(f'insert into {tbl_name} values ({emp_id},"{emp_name}",{salary})')


    elif ch == 3:
        tbl_name = input("enter a table name: ")
        print("--what do you want to update--\n"
              "1. emp_id \n"
              "2. emp_name \n"
              "3. salary")

        ch1 = int(input("enter a choice: "))

        if ch1 == 1:
            emp_id = int(input("enter new emp_id: "))
            emp_name = input("enter reference emp_name: ")
            mycursor.execute(f'update {tbl_name} set emp_id={emp_id} where emp_name ="{emp_name}";')

        elif ch1 == 2:
            emp_name = (input("enter new emp_name: "))
            emp_id = int(input("enter reference emp_id: "))
            mycursor.execute(f'update {tbl_name} set emp_name = "{emp_name}" where emp_id ={emp_id};')

        elif ch1 == 3:
            salary = int(input("enter new salary: "))
            emp_id = int(input("enter reference emp_id: "))
            mycursor.execute(f'update {tbl_name} set salary= {salary} where emp_id ={emp_id};')

    elif ch == 4:
        tbl_name = input("enter a table name: ")
        emp_id = int(input("enter a emp_id: "))

        mycursor.execute(f"delete from {tbl_name} where emp_id = {emp_id};")


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





