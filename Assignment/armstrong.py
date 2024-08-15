num = int(input("Enter number: "))
number = num
sum = 0
while(num!=0):
    remainder = num%10
    num = int(num / 10)
    sum += (pow(remainder,len(str(number))))
if(number == sum):
    print(number,"is armstrong number")
else:
    print(number,"is not a armstrong number")
    
    
