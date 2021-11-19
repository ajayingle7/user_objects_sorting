from abc import ABC,abstractmethod

class SPPU:
    @abstractmethod
    def notice1(self):
        pass

    @abstractmethod
    def notice2(self):
        pass

    @abstractmethod
    def notice3(self):
        pass

    @abstractmethod
    def notice4(self):
        pass

    def exam(self):
        print("exam are same time")

class IICMR(SPPU):
    def notice1(self):
        print("notice1")

    def notice2(self):
        print("notice2")

    def notice3(self):
        print("notice3")

    def notice4(self):
        print("notice4")

    def exam(self):
        super().exam()


class DYPATIL(IICMR):
    def notice1(self):
        print("notice1")

    def notice2(self):
        print("notice2")

    def notice3(self):
        print("notice3")

    def notice4(self):
        print("notice4")

    def exam(self):
        super().exam()


class SINHGAD(DYPATIL):
    def notice1(self):
        print("notice1")

    def notice2(self):
        print("notice2")

    def notice3(self):
        print("notice3")

    def notice4(self):
        print("notice4")

    def exam(self):
        super().exam()


obj1 = SINHGAD()
obj1.exam()

obj2 = DYPATIL()
obj2.exam()

obj3 = IICMR()
obj3.exam()


