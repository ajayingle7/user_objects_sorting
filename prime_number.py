from getpass import getpass


def f1():
    username= input("enter username: ")
    password= getpass(input("enter a password: "))

    return username,password

print(f1())


a = input("enter name:")
print(a)