#MultiLevel Inheritance

class Parent():
    def func1(self):
        print("Parent class...")

class Child1(Parent):
    def func2(self):
        print("Child class 1...")

class Child2(Child1):
    def func3(self):
        print("Child class 2...")

       
ob = Child2()
ob.func1()
ob.func2()
ob.func3()

ob2 = Child1()
ob2.func1()
ob2.func2()
