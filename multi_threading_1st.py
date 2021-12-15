from threading import Thread,current_thread

def even():
    for i in range(0,11,2):
        print(i,current_thread().name)

def odd():
    for i in range(1,11,2):
        print(i, current_thread().name)


obj1 = Thread(target=even)
obj2 = Thread(target=odd)

obj1.start()
obj2.start()