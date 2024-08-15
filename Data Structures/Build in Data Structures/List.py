#List[]
print("List......")
list1 = [8,10,19,27,30,"SB"]
print(list1)

print("\nPrint particular index data - list[index] ")
print(list1[3])

print("\nPrint inbetween the given index - list[startIndex: endIndex-1] ")
print(list1[1:4])

print("\nPrint staeting of the index 0 to endindex-1")
print(list1[:4])

print("\nPrint all datas in the list")
print(list1)
print(list1[:])

print("\nPrint using negative index")
print(list1[-1])

print("\nReplace a list data")
list1[-1] = "Siva"
print(list1)

print("\nAdd data in the end of the list")
list1.append("Balan")
print(list1)

print("\nInsert a data in a prefered index in list")
list1.insert(0,"SB") 
print(list1)

print("\nRemove the data in the given index from the list")
list1.pop(0)
print(list1)

print("\nDelete the data in the given index from the list")
del list1[0] 
print(list1,"\n")

print("\nPrint a list data seperately")
for i in list1:
    print(i)

