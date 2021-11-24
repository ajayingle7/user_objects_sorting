class A:
    __acc_no = 39032366969
    bal = 5000
    branch= "kaij"

    def __acc_info(self):
        return self.__acc_no,self.bal

obj1 = A()
obj1.bal = 500
print(obj1._A__acc_info())
print(obj1._A__acc_no)