class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h%self.MAX

    def __setitem__(self, key, value):    #def set(self, key, value):
        h = self.getHash(key)
        # print(h)
        self.arr[h] = value

    def __getitem__(self, key):  #def get(self, key):
        h = self.getHash(key)
        return self.arr[h]

    def __delitem__(self, key):  #def del(self, key):
        h = self.getHash(key)
        self.arr[h] = None

ht = HashTable()
ht['july 8'] = 10 # ht.set('july 8', 10)
ht['june 12'] = 12 # ht.set('june 12', 12)
ht['march 6'] = 27 # ht.set('march 6', 27)
print(ht['march 6'])# print(ht.get('june 12'))
print(ht['july 8'])# print(ht.get('july 8'))
print(ht['june 12'])# print(ht.get('june 12'))
print(ht['march 6'])# print(ht.get('march 6'))
del ht['march 6']
print(ht.arr)