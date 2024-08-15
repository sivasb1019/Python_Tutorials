#Multiple Inheritance

class Parent1():
    def func1(self):
        print("Parent class 1...")

class Parent2():
    def func2(self):
        print("Parent class 2...")
        
class Child(Parent1,Parent2):
    def func3(self):
        print("Child class...")
ob = Child()
ob.func1()
ob.func2()
ob.func3()
