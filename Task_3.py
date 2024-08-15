class String():
    def __init__(self, data):
        self.input = data

    def display(self):
        if (type(self.input) == str):
            print(f"{self.input} UpperCase of this String=", self.input.upper())
            print(f"{self.input} lowerCase of this String=", self.input.lower())
            print(f"{self.input} Title  of this String=", self.input.title())
            print(f"{self.input} SwapCase  of this String=", self.input.swapcase())
            print(f"{self.input} Capitalize  of this String=", self.input.capitalize())
            print(f"{self.input} Casefold  of this String=", self.input.casefold())
            print(f"{self.input} Center  of this String=", self.input.center(14))
            print(f"{self.input} Center  of this String=", self.input.center(17, '/'))
            print(f"{self.input} Count  of this String=", self.input.count('a'))
            print(f"{self.input} endWith  of this String=", self.input.endswith('aNa'))
            print(f"{self.input} endWith  of this String=", self.input.endswith('aN', 5, 7))
            print(f"{self.input} expendtab of this String=", self.input.expandtabs(4))
            print(f"{self.input} find the sring in given input=", self.input.find('K'))
            print(f"{self.input} index of this String=", self.input.index('aKs'))
            print(f"{self.input} alpnum  of this String=", self.input.isalnum())
            print(f"{self.input} ", self.input.isdigit())
            print(f"{self.input} valid identifier  of this String=", self.input.isidentifier())
            print(f"{self.input} ", self.input.islower())
            print(f"{self.input} ", self.input.isupper())
            print(f"{self.input} ", self.input.isspace())
            print(f"{self.input} ", self.input.istitle())
            print(f"{self.input} ", self.input.lstrip())
            print(f"{self.input} ", self.input.rstrip('k'))
            print(f"{self.input} replace of this string", self.input.replace('KsH', 'lux'))
        else:
            print("Its not string function")
        print("-".join(self.input))


String_1 = String("LaKsHaNa123k")
String_1.display()
String_2 = String(['l', 'a', 'k', 's', 'h'])
String_2.display()
