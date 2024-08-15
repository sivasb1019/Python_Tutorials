class laptop:
    def __init__(self):
        self.modelName = ""
        self.modelPrice = 0
        self.modelProcessor = ""
        self.modelRam = ""
    def lapDetails(self):
        print(f"Model Name      : {self.modelName}")
        print(f"Model Price     : {self.modelPrice}")
        print(f"Model Processor : {self.modelProcessor}")
        print(f"Model RAM       : {self.modelRam}\n")

hp =laptop()
hp.modelName = "HP Pavilion"
hp.modelPrice = 70000
hp.modelProcessor = "i5"
hp.modelRam = "128GB"
hp.lapDetails()

dell =laptop()
dell.modelName = "Dell"
dell.modelPrice = 80000
dell.modelProcessor = "i5"
dell.modelRam = "128GB"
dell.lapDetails()
