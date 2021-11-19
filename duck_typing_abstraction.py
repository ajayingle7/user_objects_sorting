from abc import ABC,abstractmethod

class DB(ABC):
    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass

class Oracle(DB):

    def commit(self):
        print("commit--oracle")

    def rollback(self):
        print("rollback--oracle")


class Mysql(DB):
    def commit(self):
        print("commit--mysql")

    def rollback(self):
        print("rollback--mysql")

def connect(para):
    para.commit()
    para.rollback()

connect(Oracle())
connect(Mysql())