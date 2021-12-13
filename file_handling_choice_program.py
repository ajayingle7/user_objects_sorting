print("1.read\n"
      "2.write\n"
      "3.append \n"
      "4.close")
while True:
    choice = int(input("enter choice: "))

    if choice == 1:
        fb = open("C:\\Users\\ajayi\\OneDrive\\Desktop\\abcd.txt", "rt")
        print(fb.read())

    elif choice == 2:
        fb = open("C:\\Users\\ajayi\\OneDrive\\Desktop\\abcd.txt", "wt")
        enter = input("enter lines: ")

        fb.write(enter)


    elif choice == 3:
        fb = open("C:\\Users\\ajayi\\OneDrive\\Desktop\\abcd.txt", "at")
        enter1 = input("append a line: ")

        fb.write(enter1)

    elif choice == 4:
        fb = open("C:\\Users\\ajayi\\OneDrive\\Desktop\\abcd.txt")
        fb.close()
        print("file closed")
        break


    else:
        print("wrong choice")
