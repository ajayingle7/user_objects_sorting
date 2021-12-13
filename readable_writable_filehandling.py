with open("text1.txt","rt") as fb:
    print(fb.read())








f= open("text1.txt",'rt')

try:
    print("readable: ", f.readable())
    print("writable: ", f.writable())


    if f.readable():
        print(f.read())
    else:
        print("file is not reading mode")

    if f.writable():

        f.write("MONDAY\n TUESDAY\n WEDNSEDAY\n THURSEDAY\n FRIDAY\n SATUARDAY")


    else:
        print("file is not in writing mode")


finally:
    f.close()




