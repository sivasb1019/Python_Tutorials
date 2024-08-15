#file1 = open("file1.txt","x")
#read a file
'''file = open("E:/Python Training/Assingment.txt","w")
file.write("Siva ")
file.write("Balan ")
file.write("V")
file.write("\n")
file.write("B.E-CSE")
file = open("E:/Python Training/Assingment.txt","a")
file.write("\n1019")
file.close()'''
f = open("fruits.txt", "r+")
f.write("Apple\n")


print(f.read())
f.close()

f = open("fruits.txt","r")
print(f.read())

