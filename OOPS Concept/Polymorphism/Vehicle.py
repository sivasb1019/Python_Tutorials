class Vehicles():
    def start(self):
        print("Vehicle started")
class Car(Vehicles):
    def start(self):
        print("Car started")

vehicle = Vehicles()
vehicle.start()

car = Car()
car.start()
