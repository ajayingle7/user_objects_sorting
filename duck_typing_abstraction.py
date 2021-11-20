
class IICMR:

    def MCA(self):
        mca = "master of computer application"
        return mca
    def MBA(self):
        mba = "master of busniness administration"
        return mba
    def BBA(self):
        bba = "bachlore of business administration"
        return bba

class DYPATIL:
    def MCA(self):
        mca = "master of computer application"
        return mca

    def MBA(self):
        mba = "master of busniness administration"
        return mba

    def BBA(self):
        bba = "bachlore of business administration"
        return bba


class JSPM:
    def MCA(self):
        mca = "master of computer application"
        return mca

    def MBA(self):
        mba = "master of busniness administration"
        return mba

    def BBA(self):
        bba = "bachlore of business administration"
        return bba

class SYMBOSYS:
    def MCA(self):
        mca = "master of computer application"
        return mca

    def MBA(self):
        mba = "master of busniness administration"
        return mba

    def BBA(self):
        bba = "bachlore of business administration"
        return bba
class IMCC:
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
myfun(IICMR())
myfun(JSPM())
myfun(DYPATIL())
myfun(SYMBOSYS())