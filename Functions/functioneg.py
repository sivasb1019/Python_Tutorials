'''#abs Function():
d=1+10j
x=abs(d)
print("Value of a complex number for",d,"is",x)

#enumerate function():
a = ("apple","orange")
x=enumerate(a)
print("a: ",tuple(x))

#format function():
a=0.1
print("Percentage of",a,": ",format(a,'%'))

#id function():
c=10
print("ID of ",c,": ",id(c))

#getattr & setattr function():
class person():
    name = "SB"
    age = 21
    place = "Tuty"
print("Person Name: ",getattr(person,'name'))
print("Person Age: ",getattr(person,'age'))
print("Person Place: ",getattr(person,'place'))
print("Pesson Place is changed to: ",setattr('place','Thoothukudi'))

#min, max and sorted function():
l=[30,27,8,19,10,3,11,12]
print("Minimum value in list l:",min(l))
print("Maximum value in list l:",max(l))
print("Sorted list of l: ",sorted(a))'''

#lambda function
a = int(input("Enter a: "))
b = int(input("Enter b: "))
output1 = lambda x,y:x+y # x = a , y = b
output2= lambda y,x:x+y+10 # x = b , y = a
print(output1(a,b))
print(output2(a,b))
      
