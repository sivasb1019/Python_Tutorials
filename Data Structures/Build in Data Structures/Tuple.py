#tuple()

a = 10,
print(type(a))

#Emplty tuple
tuple1 = ()

tuple1 = (10.00,19,27,"Siva","Balan")
print("tuple1:",tuple1)
print(tuple1[1])
print(tuple1[1:3])
print(tuple1[-2])
print(tuple1[:])
print()
#To change tuple value
list1 = list(tuple1)
print("list1:",list1)
list1[0] = 10
list1[4] = "SB"
print("list1:",list1)
print()
tuple1 = tuple(list1)
print("tuple1:",tuple1)
