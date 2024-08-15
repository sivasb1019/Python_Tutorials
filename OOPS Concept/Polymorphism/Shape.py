class Shape():
    def area(self):
        return 0
class Rectangle(Shape):
    def area(self,l,b):
        return l*b

shape = Shape()
print(shape.area())

rec = Rectangle()
print("Area of rectangle:",rec.area(8,10))
