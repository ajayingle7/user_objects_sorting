from threading import Thread
class Myclass(Thread):

    def __init__(self,a):
        Thread.__init__(self)
        self.a = a

    def run(self):
        for i in range(self.a,10,2):
            print(i)

class Myclass2(Thread):
    def __init__(self,a):
        Thread.__init__(self)
        self.a = a
        Thread.__init__(self)
    def run(self):
        for i in range(self.a,10,2):
            print(i)

obj1= Myclass(0)
obj2= Myclass2(1)

obj1.start()
obj2.start()

