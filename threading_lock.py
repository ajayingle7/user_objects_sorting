from threading import Thread,Lock,current_thread

l = Lock()

def m1(name):
    for i in range(5):
        l.acquire()
        print("[")
        print(name)
        print("]")
        l.release()
t1 = Thread(target=m1,args=("python",))
t2 = Thread(target=m1, args=("java", ))

t1.start()
t2.start()
