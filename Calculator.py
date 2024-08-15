def add():
    n = int(input("How many numbers do you want to add: "))
    sum = 0
    for i in range(n):
        print("Enter number",i+1,":", end =" ")
        num = int(input())
        sum = sum + num
    print("\nAddition of above numbers:", sum)

def sub():
    n = int(input("How many numbers do you want to subract: "))
    subract = 0
    for i in range(n):
        print("Enter number",i+1,":", end =" ")
        num = int(input())
        subract = num - subract
    print("\nSubraction of above numbers:", subract)

def mul():
    n = int(input("How many numbers do you want to multiply: "))
    multiply = 1
    for i in range(n):
        print("Enter number",i+1,":", end =" ")
        num = int(input())
        multiply = multiply * num
    print("\nMultiplication of above numbers:", multiply)

def div():
    n = int(input("How many numbers do you want to divide: "))
    print("Enter number 1 :", end =" ")
    divide = int(input())
    for i in range(1,n):
        print("Enter number",i+1,":", end =" ")
        num = int(input())
        divide = divide / num
    print("\nDivision of above numbers:", divide)
print("1.Addition 2.Subraction 3.Multipy 4.divide?")
calc = int(input("Enter option 1 or 2 or 3 or 4: "))
if(calc == 1):
    add()
elif(calc == 2):
    sub()
elif(calc == 3):
    mul()
elif(calc == 4):
    div()
else:
    print("Invalid Option")
