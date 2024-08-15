class Person():
    def __init__(self,name):
        self.name = name
class Student(Person):
    def __init__(self,name,grade):
        self.grade = grade
        super().__init__(name)
    def details(self):
        print("Name:",self.name)
        print("Grade:",self.grade)

siva = Student("Siva","O+")
siva.details()
