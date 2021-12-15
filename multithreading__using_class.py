from threading import Thread,current_thread
class Even(Thread):
    def __init__(self,a,b):
        self.a = a
        self.b = b

        Thread.__init__(self)

    def run(self):
        for i in range(self.a,self.b,2):
            print(i,current_thread().name)

class Odd(Thread):
    def __init__(self,a,b):
        self.a = a
        self.b = b

        Thread.__init__(self)

    def run(self):
        for i in range(self.a,self.b,2):
            print(i,current_thread().name)


t1 = Even(0,11)
t2 = Odd(1,11)

t1.start()
t2.start()