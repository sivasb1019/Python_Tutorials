class Person():
    def __init__(self):
        self._experience = "1 year"
        self.__name = "Siva"
        
    def fresher(self):
        self.__name = "Siva Balan"
        self._experience ="Fresher"
        print("Name:",self.__name)
        print("Experience:",self._experience)
class Experience(Person):
    pass 
print("Person class...")
siva = Person()
print(siva._experience)
siva.fresher()
print(siva._experience)

print("Experience class...")
sb = Experience()
print(sb._experience)
print(siva.__name)
