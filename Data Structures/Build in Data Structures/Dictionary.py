dic = {"Name":"SB",
       "age":21,
       }
print("dic:",dic)
print(dic.keys())

#To replace a value
dic["Name"] = "Siva Balan"
print("Replacing name:",dic)

#To add new key and value
dic["Blood"] = "O+ve"
print(dic)
dic.update({"Weight":59})
print(dic)

#To get keys
print(dic.keys())

#To get values
print(dic.values())

#To delete key and value
del dic["Weight"]
print(dic)

#To print key and value seperately
for key,value in dic.items():
    print("Key:",key)
    print("Value:",value)
