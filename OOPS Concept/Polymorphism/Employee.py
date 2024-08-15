class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self,name,salary,department):
        self.dept = department
        super().__init__(name,salary)
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.dept)

manager = Manager("Siva",60000,"Software Developer")
manager.display()
