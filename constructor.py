class A:
    def __init__(self, name,surename,birthdate,address,telephone,email):
        self.name = name
        self.surename = surename
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

    def display(self):
        return "name is:{} ,surename:{} ,address:{} , teplephone :{} ,email: {}".format(self.name,self.surename,self.birthdate,self.address,self.telephone,self.email)

obj = A("Ajay","ingle","12-03-1998","pune",7770078554,"ajayingle109@gmail.com")
print(obj.display())
print(obj.name)
print(obj.email)