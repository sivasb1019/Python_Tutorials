#1. Write a program to computr the sum of the n natural numbers.
'''
sum=0
n = int(input("Enter n: "))
for i in range(1,n+1):
    sum+=i
print("Sum of 5 natural numbers:",sum)'''

#2. Write a program to read 10 numbers from the keyboard and find their sum and average.
'''
sum=0
a = []
for i in range(10):
    num = int(input("Enter number "+str(i+1)+":"))
    a.append(num)
print("List of a:",a)
for i in a:
    sum+=i
average=sum/10
print("Sum of the 10 numbers:",sum)
print("Average of the 10 numbers:",average)'''

#3. Write a program to display the cube of the number upto an integer.

n = int(input("Enter n: "))
for i in range(1,n+1):
    print("Number:",i,"and cube of the",i,"is",i*i*i)
