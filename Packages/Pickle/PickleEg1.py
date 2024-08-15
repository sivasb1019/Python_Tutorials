import pickle

mydict = {"1" : "a", "2" : "b"}

print("Pickling without a file:")
a = pickle.dumps(mydict)
print("Dumping with Pickle:",type(a))
dict1 = pickle.loads(a)
print("Loading with Pickle:",type(dict1),dict1)

print("\nPickling with a file:")
pickleFile = open("picklefile", "wb")
pickle.dump(mydict, pickleFile)
print("Dumping with Pickle:")
pickleFile.close()
pickleFile1 = open("picklefile","rb")
newdict = pickle.load(pickleFile1)
print("Loading with Pickle:",newdict)
pickleFile.close()
