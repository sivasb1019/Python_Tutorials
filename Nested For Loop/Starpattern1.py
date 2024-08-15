#1. Print:
'''
      *
      * *
      * * *
      * * * *
      * * * * *
'''
for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()

#2.Print:
'''
     1
     1 2
     1 2 3
     1 2 3 4
     1 2 3 4 5
'''
for i in range(6):
    for j in range(i):
        print(j+1,end=" ")
    print()
