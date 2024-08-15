#Example 1: Print 2 multiply table(1-10).
'''
for i in range(1,11):
    print("2 x",i,"=",2*i)'''

#Example 2: Input 2 nos and print the numbers between them.
'''
a = int(input("Enter a: "))
b = int(input("Enter b: "))
for i in range(a,b):
    print(i)'''

#Example 3: Print even numbers between 1 to 10.
'''
for i in range(1,11):
    if(i%2==0):
        print(i)'''

#Example 4: Count the odd numbers between 1 to 10.
'''
count=0
for i in range(1,11):
    if(i%2!=0):
        count+=1
print(count)'''

#Example 4: Count the even and odd numbers between 1 to 10.
'''
Ecount = 0
Ocount = 0
for i in range(1,11):
    if(i%2==0):
        Ecount+=1
    else:
        Ocount+=1
print("Number of even numbers between 0 to 10:",Ecount)
print("Number of odd numbers between 0 to 10:",Ocount)'''

#Example 6: count the number which are divisible by 3 and 5.
count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count+=1
print("Counts of the number divisible by 3 and 5:",count)
