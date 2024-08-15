#Hybrid Inheritance

class Parent():
    def func1(self):
        print("Parent class...")

class Child1(Parent):
    def func2(self):
        print("Child class 1...")

class Child2(Parent):
    def func3(self):
        print("Child class 2...")

class Child3(Child1):
    def func4(self):
        print("Child class 3...")

class Child4(Child3,Child2):
    def func5(self):
        print("Child class 4...")

print("Child 1 Object..")
ob = Child1()
ob.func1()
ob.func2()

print("\nChild 2 Object..")
ob = Child2()
ob.func1()
ob.func3()

print("\nChild 3 Object..")
ob = Child3()
ob.func1()
ob.func2()
ob.func4()

print("\nChild 4 Object..")
ob = Child4()
ob.func1()
ob.func2()
ob.func3()
ob.func4()
ob.func5()
