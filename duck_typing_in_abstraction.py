from abc import ABC,abstractmethod
class IICMR(ABC):
    @abstractmethod
    def MCA(self):
        mca = "master of computer application"
        return mca
    @abstractmethod
    def MBA(self):
        mba = "master of busniness administration"
        return mba
    @abstractmethod
    def BBA(self):
        bba = "bachlore of business administration"
        return bba

class DYPATIL(IICMR):
    def MCA(self):
        mca = "master of computer application"
        return mca

    def MBA(self):
        mba = "master of busniness administration"
        return mba

    def BBA(self):
        bba = "bachlore of business administration"
        return bba


class JSPM(IICMR):
    def MCA(self):
        mca = "master of computer application"
        return mca

    def MBA(self):
        mba = "master of busniness administration"
        return mba

    def BBA(self):
        bba = "bachlore of business administration"
        return bba

class SYMBOSYS(IICMR):
    def MCA(self):
        mca = "master of computer application"
        return mca

    def MBA(self):
        mba = "master of busniness administration"
        return mba

    def BBA(self):
        bba = "bachlore of business administration"
        return bba
class IMCC(IICMR):
    def MCA(self):
        mca = "master of computer application"
        return mca

    def MBA(self):
        mba = "master of busniness administration"
        return mba

    def BBA(self):
        bba = "bachlore of business administration"
        return bba


def myfun(obj):
    print(obj.MCA())
    print(obj.MBA())
    print(obj.BBA())

myfun(IMCC())
myfun(JSPM())
myfun(DYPATIL())
myfun(SYMBOSYS())