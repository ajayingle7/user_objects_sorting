from abc import ABC,abstractmethod

class RBI(ABC):
    def __init__(self,rbi_head):
        self.rbi_head= rbi_head



    @abstractmethod
    def rule1(self):
        deposit = 25000

    @abstractmethod
    def rule2(self):
        commision_per = 10

    @abstractmethod
    def rule3(self):
        age = 18

    @abstractmethod
    def rule4(self):
        ineterest_per = 15

    @abstractmethod
    def rule5(self):
        loan_limit = 10000000

    def notice(self):
        print("hello this is only notice for applying all rules same as given in all bank")

class SBI(RBI):
    def rule1(self):
        print("our deposit is 25000")

    def rule2(self):
        print("commision method is 10 percent")


    def rule3(self):
        print("age above 18")

    def rule4(self):
        print("our interest percentage is 15 percent")

    def rule5(self):
        print("loan limit till 10000000")

    def notice(self):
        print("hello this is only notice for applying all rules same as given in all bank")

    def __init__(self,rbi_head):
        self.rbi_head = rbi_head
        super().__init__(self.rbi_head)
        print(rbi_head)

    def SBI_rule(self):
        print("this is only sbi rule")

class AXIS(RBI):
    def __init__(self,rbi_head):
        self.rbi_head = rbi_head
        super().__init__(rbi_head)
        print(rbi_head)

    def rule1(self):
        print("desposit of axis is 250000")

    def rule2(self):
        print("commision of axis is 10")

    def rule3(self):
        print("age is above 18")

    def rule4(self):
        print("interest is 15 percent")

    def rule5(self):
        print("loan is above 10000000")

    def axis_rule(self):
        print("this is only axis rule")




obj1 = SBI("finance_ministry_of_india")
obj1.rule1()
obj1.rule2()
obj1.rule3()
obj1.rule4()
obj1.rule5()
obj1.notice()
obj1.SBI_rule()

obj2 = AXIS("finiance ministry of india")
obj2.rule1()
obj2.rule2()
obj2.rule3()
obj2.rule4()
obj2.rule5()
obj2.axis_rule()