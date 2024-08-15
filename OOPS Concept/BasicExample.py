class Person:   # Creating a class
    gender = "unknown"
    def __init__(self, name, age, role):    # init method or constructor method
        self.name = name
        self.age = age
        self.role = role

    @classmethod
    def c(cls):
        cls.gender = 'Male' # cls = Person




    def myDetails(self):    # Method creation
        print("Name",self.name)
        print("Age:",self.age)
        print("Role:",self.role)
        print("Gender:",self.gender)


person1 = Person("Siva Balan",21,"King")
person1.myDetails()  # Person.myDetails(person1)
Person.c()
person1.myDetails()  # Person.myDetails(person1)
person2 = Person("SB",21,"Apprentice of King")
person2.myDetails()

