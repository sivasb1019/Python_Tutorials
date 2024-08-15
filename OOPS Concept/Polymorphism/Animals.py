class Animal():
    def sound(self):
        print("Animal makes soung")
class Dog(Animal):
    #Method Overriding (Overriding the Animal sound() function)
    def sound(self):
        print("Dog Barks")
class Bird(Animal):
    #Method Overriding (Overriding the Animal sound() function)
    def sound(self):
        print("Bird Sing")
animal = Animal()
animal.sound()
dog = Dog()
dog.sound()
bird = Bird()
bird.sound()
    
