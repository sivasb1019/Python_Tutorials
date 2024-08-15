class Laptop:
    chargerType = "C type"

    def __init__(self):
        self.brand = ""
        self.price = 0

    def setBrand(self, brand):
        self.brand = brand

    def getBrand(self):
        print(self.brand)

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        print(self.price)

    def details(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


    @classmethod
    def changeChargerType(cls):
        cls.chargerType = "B type"
        print("Charger type is changed to b type")

    @staticmethod
    def info():
        print("This is laptop class")


hp = Laptop()
hp.details()
hp.brand = "lakshu"
hp.details()
hp.setBrand("HP")
hp.getBrand()
hp.setPrice(300)
hp.getPrice()
hp.changeChargerType()