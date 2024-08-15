#An iterable user defined type
class myClass:
    #constructor
    def __init__(self,limit):
        self.limit = limit
    #Creating iterator object which is called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self
    #To iterate over the next element, we creates __next__
    def __next__(self):
        #Storing current value of x
        x= self.x
        #Stop iteration if limit is reached
        if x>self.limit:
            raise StopIteration
        #else increment and return x
        self.x = x+1;
        return x

for i in myClass(19):
    print("................")
    print(i)
print("\n")
for i in myClass(6):
    print(i)
