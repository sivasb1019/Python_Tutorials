#String

name = "Siva Balan V"
print("Name:",name)
print("Name Length:",len(name))
print("Sliced Name:",name[5:10])
print("Uppercase:",name.upper())
print("Lowercase:",name.lower())
print("Replaced Name:",name.replace("V","SB"))
print("Reversed Name:",name[::-1])
for i in name:
    if(i == "a"):
        continue
    print(i)
