class Main():
    def cust_data(self, name, address):
        self.name = name
        self.address = address

        print("name is ", self.name)
        print("address is", self.address)

    def room_mate(self, numbers):
        self.total1 = numbers * 3000
        return f"room rent: {self.total1}"

    def resturant(self):
        tea = int(input("tea: "))
        water = int(input("water: "))
        lunch = int(input("lunch: "))

        tea1 = tea * 20
        water1 = water * 20
        lunch1 = lunch * 300

        self.total2 = tea1 + water1 + lunch1

        return f" resturent bill is  {self.total2}"

    def laundry(self):
        shirt = int(input("shirt quantity : "))
        trouser = int(input("trouser quantity : "))
        blanket = int(input("blanket quantity : "))
        bedsheet = int(input("bedsheet quantity: "))
        shirt1 = shirt * 20
        trouser1 = trouser * 40
        blanket1 = blanket * 100
        bedsheet1 = bedsheet * 100

        self.total3 = shirt1 + trouser1 + blanket1 + bedsheet1

        return f" laundry bill is  {self.total3}"

    def game(self):
        print("game is 100 RS per hour")

        pubg = int(input("enter pubg game hour : "))
        football = int(input("enter football game hour : "))
        pokemon = int(input("enter pokemon game hour : "))
        boxing = int(input("enter boxing game hour : "))

        pubg1 = pokemon * 100
        football1 = football * 100
        pokemon1 = pokemon * 100
        boxing1 = boxing * 100

        self.total4 = pubg1 + football1 + pokemon1 + boxing1

        return f" game bill is  {self.total4}"

    def bill_total(self):
        print("Customer_Name: ", self.name)
        print("Customer_Address:", self.address)

        print("Total Room Rent Bill: ", self.total1)
        print("Total Resturent Bill: ", self.total2)
        print("Total laundry Bill: ", self.total3)
        print("Total game bill: ", self.total4)

        print("Total bill: ", self.total1 + self.total2 + self.total3 + self.total4)


obj1 = Main()

while True:
    print("WELCOME TO HEAVEN HOTEL\n"
          "1. ENTER CUSTOMER DATA\n"
          "2. ENTER ROOMMATES \n"
          "3. CALCULATE RESTURANT BILL\n"
          "4. CALCULATE LAUNDRY BILL \n"
          "5. CALCULATE GAME BILL \n"
          "6. SHOW TOTAL COST \n "
          "7.EXIT")

    choice = int(input("ENTER YOUR OPTION HERE: "))

    if choice == 1:
        name = input("enter name: ")
        address = input("enter address: ")

        obj1.cust_data(name, address)

    elif choice == 2:
        numbers = int(input("enter number of members: "))
        print(obj1.room_mate(numbers))

    elif choice == 3:
        print(obj1.resturant())

    elif choice == 4:
        print(obj1.laundry())

    elif choice == 5:
        print(obj1.game())

    elif choice == 6:
        obj1.bill_total()


    elif choice==7:
        break


    else:
        print("choose right choice ")

