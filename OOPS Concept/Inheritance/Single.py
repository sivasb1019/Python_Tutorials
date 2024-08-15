#Single Inheritance

class Parent():
    def func1(self):
        print("Parent class...")

class Child(Parent):
    def func2(self):
        print("Child class...")
ob = Child()
ob.func1()
ob.func2()
