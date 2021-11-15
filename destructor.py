class B:

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"{self.name}, {self.contact}"

    def __del__(self):
        print("object is deleted successfully")

b = B("vijay", 7770078554)
del b




