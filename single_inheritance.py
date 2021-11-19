
from abc import ABC, abstractmethod

class DB(ABC):
    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        print("update")

    def delete(self):
        print("delete")

class Mysql(DB):
    def commit(self):
        print("commit")

    def rollback(self):
        print("rollback")

    def insert(self):
        print("imsert")
    def update(self):
        print("update")


class Oracle(DB):
    def commit(self):
        print("commit")

    def rollback(self):
        print("rollback")

    def insert(self):
        print("imsert")

    def update(self):
        print("update")

    def delete(self):
        print("oracle delete")
        super().update()


obj1 = Oracle()
obj1.delete()
