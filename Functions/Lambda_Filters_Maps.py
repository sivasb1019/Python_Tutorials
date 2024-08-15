#Lamba

print("Lambda:")
x = lambda a,b,c=0 : a+b+c
print(x(19,27))
print(x(10,19,27))

#Filter

print("\nFilter:\nEg1.....")
def prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
        else:
            return True

primeNum = filter(prime,range(10))
for i in primeNum:
    print(i)

print("Eg2....")
l = [1,2,3,4,5,6,7,8,9,10]
even = filter(lambda num : num%2 == 0,l)
print(tuple(even))

#Map

print("\nMap:")
def cube(num):
    return num*num*num

list1 = [1,2,3,4,5]
cubenumber = map(cube,list1)
print(list(cubenumber))
