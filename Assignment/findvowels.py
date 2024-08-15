a = input("Enter anything: ")
print("Vowels in a:")
j=0
for i in a.lower():
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        print("a[",j,"]:", i)
    j+=1
    
