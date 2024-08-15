def add():
    return 0

def add(a):
    return a

def add(a, b):
    return a+b

def add(a, b, c):
    return a+b+c

# def add(a=0, b=0, c=0):
#     return a+b+c

sum = add(1,2,3)
print(sum)
print(add())
print(add(10))
print(add(10, 19))
print(add(10, 19, 12))