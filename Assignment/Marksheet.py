def marksheet(name,mark):
    print("Name  :",name)
    print("Mark  :",mark)
    print("Grade :",grade(mark))
    print()
    print()
def grade(mark):
    if(mark>=90):
        return "A+"
    elif(mark>=80 and mark<90):
        return "A"
    elif(mark>=70 and mark<80):
        return "B+"
    elif(mark>=60 and mark<70):
        return "B+"
    elif(mark>=40 and mark<60):
        return "C"
    else:
        return "F"
n = int(input("Number of students: "))
print()
for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: ",))
    print()
    marksheet(name,marks)
