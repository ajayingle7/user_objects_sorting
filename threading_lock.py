from threading import Thread,Lock
l = Lock()

def f1():
    l.acquire()
    name = input("enter name: ")
    surename = input("enter surename: ")
    age= int(input("enter age"))
    print(name,surename,age)
    l.release()

def f2():
    l.acquire()
    email = input("enter email: ")
    mno = int(input("enter a mno: "))
    print(email,mno)
    l.release()


t1 = Thread(target=f1)
t2 = Thread(target=f2)

t1.start()
t2.start()