'''a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = a * b * c
e = a + b + c
f = d // e
print(f)'''

'''name=input()
score=int(input())
dept=input()
print("name:",name)
print("Score:",score//10,"/10")
print("dept",dept)'''

'''meghna=input()
if(meghna=="died"):
    print("Surya meets priya")
else:
    print("surya weds meghna")
'''

# mark = int(input("Enter Mark: "))
# if mark > 35:
#     print("pass")
# else:
#     print("fail")

# income = int(input("Enter Income: "))
# if income > 7000:
#     print("Scholarship is Available")
# else:
#     print("not eligible for scholarship")

# number = int(input("Enter number: "))
# if number % 3 == 0 and number % 5 == 0: print("Good")
# else: print("Not Good")

# num = int(input("Enter number: "))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

# score = int(input("Enter Score: "))
# if score < 35: print("need to improve")
# elif 35 < score < 70: print("Good,Do Better")
# else: print("Best one")

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# print("Operations: add or sub or mul or div")
# calc = input("Enter operation: ")
# if calc == "add": print(f"Addition of {a} + {b}:", a + b)
# elif calc == "sub": print(f"Subtraction of {a} + {b}:", a - b)
# elif calc == "mul": print(f"Multiplication of {a} + {b}:", a * b)
# elif calc == "div": print(f"Division of {a} + {b}:", a // b)
# else: print("Sorry, Operation not found")

# salary = int(input("Enter Salary: "))
# age = int(input("Enter age: "))
# if salary >= 2000 or age <= 25:
#     amt = int(input("Enter amount: "))
#     if amt <= 50000: print("You are eligible for loan")
#     else: print("max loan amt is 50000")
#
# else: print("you are not eligible for loan")


# num = int(input("Enter number: "))
# limit = int(input("Enter limit: "))
# for i in range(1, limit + 1):
#     print(f"{num} x {i} = ", num * i)

# a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# for i in range(a+1, b): print(i)

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# for i in range(a, b):
#     if i % 2 == 0: print(i)

# count=0
# for i in range(1,20):
#     if(i%2!=0):
#         count+=1
# print(count)

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# even = 0
# odd = 0
# for i in range(a, b):
#     if i % 2 != 0: odd += 1
#     else: even += 1
# print("odd=", odd)
# print("even=", even)

# count=0
# for i in range(1,100):
#     if(i%3==0 and i%5==0):
#         count+=1
# print(count)

'''count=0
for i in range(1,6):
    count+=i
print(count)
'''

# n = int(input("Enter number: "))
# a = []
# sum = 0
# for i in range(1, n + 1):
#     a.append(i)
#     if i <= 7: sum += i
#
# print(a)
# print(sum)

'''n=int(input("Enter number"))
for i in range(n):
    print(i**3)'''

# for i in range(1,3):
#     print("Week: ",i)
#     for j in range(1,8):
#         print("   Day: ",j)

# n = int(input("Enter number: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# for i in range(1,6):
#     print()
#     for j in range(1,i+1):
#         print("*",end=" ")

# i=1
# while(i<=5):
#     print(i)
#     i+=1

# i=10
# while(i<=100):
#     print(i,end=",")
#     i+=10

# n = int(input("Enter number: "))
# while n >= 1:
#     print(n, end=", ")
#     n -= 1

n = int(input("Enter number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(f"Factorial of {n}", fact)
