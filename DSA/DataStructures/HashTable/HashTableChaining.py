class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h%self.MAX

    def __setitem__(self, key, value):    #def set(self, key, value):
        h = self.getHash(key)
        # print(h)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):  #def get(self, key):
        h = self.getHash(key)
        if self.arr[h] is None:
            return "key not found"
        if len(self.arr[h]) > 1:
            for element in self.arr[h]:
                if key == element[0]:
                    found = True
                    return  element[1]

        return self.arr[h][0][1]

    def __delitem__(self, key):  #d ef del(self, key):
        h = self.getHash(key)
        for index, element in enumerate(self.arr[h]):
            if key == element[0]:
                del self.arr[h][index]

ht = HashTable()
ht['july 8'] = 10 # ht.set('july 8', 10)
ht['june 12'] = 12 # ht.set('june 12', 12)
ht['march 6'] = 27 # ht.set('march 6', 27)
ht['march 17'] = 19 # ht.set('march 17', 19)
print(ht['june 12'])# print(ht.get('june 12'))
# print(ht['july 8'])# print(ht.get('july 8'))
# print(ht['june 12'])# print(ht.get('june 12'))
print(ht['march 6'])# print(ht.get('march 6'))
print(ht['march 17'])# print(ht.get('march 17'))
print(ht.arr)
del ht['march 6']
print(ht.arr)