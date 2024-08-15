c=5
for i in range(6):
    for j in range(c,0,-1):
        print(end=" ")
    c-=1
    for k in range(i):
        print(i,end=" ")
    print()

