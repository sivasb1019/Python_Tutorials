#Hierarchical Inheritance

class Parent():
    def func1(self):
        print("Parent class...")

class Child1(Parent):
    def func2(self):
        print("Child class 1...")

class Child2(Parent):
    def func3(self):
        print("Child class 2...")

ob = Child1()
ob.func1()
ob.func2()
     
ob = Child2()
ob.func1()
ob.func3()
