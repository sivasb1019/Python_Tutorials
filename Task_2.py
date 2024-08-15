a=[1,2,3,4,5]
a1=[12,13,14]
b=("A","B","C","D")
c={20,30,40}
d={"name":"lakshana","age":22,"location":"tuty"}
def displayList():
    print(a)
    a.append(7)
    print(a)
    a.append("TCARE")
    print(a)
    print(a[0])
    print(a[2:5]) 
    a.insert(0,10)
    print(a)
    a[0]=11
    print(a)
    a.pop(4)
    print(a)
    a.extend(a1)
    print(a)

def displayTuple():
    b1 = list(b)
    b1.remove("A")
    b2 = tuple(b1)
    print(b2)

    b3 = list(b)
    b3.pop()
    b4 = tuple(b3)
    print(b4)
        
def displaySet():
    c.add(50)
    c.remove(30)
    c.pop()
    print(c)
    
def displayDic():
    print(d)
    print(d.keys())
    print(d.values())
    d.update({"age":23})
    print(d)
    del d["location"]
    print(d)
    d.clear()
    print(d)
    
displayList()
displayTuple()
displaySet()
displayDic()
