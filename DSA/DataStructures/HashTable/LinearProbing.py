class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def getHash(self,key):
        h = 0
        for char in key:
            h +=  ord(char)
        return  h % self.MAX

    def __getitem__(self, key):
        h = self.getHash(key)
        if self.arr[h] is None:
            return  f"{key} is not present..."
        prob_range = self.getProbRange(h)
        for index in prob_range:
            element = self.arr[index]
            if element is None:
                # print(self.arr[index])
                return f"{key} is not present..."
            if element[0] == key:
                return  element[1]

    def __setitem__(self, key, value):
        h = self.getHash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, value)
        # elif self.arr[h][0] == key:
        #     self.arr[h] = (key, value)
        else:
            h = self.findSlot(key, h)
            self.arr[h] = (key, value)
        # print(h, value, type(h))

    def getProbRange(self, index):
        return [*range(index, self.MAX)] + [*range(0, index)]

    def findSlot(self, key, index):
        prob_range = self.getProbRange(index)
        # print(prob_range)
        for prob_index in prob_range:
            # print(self.arr[prob_index], type(prob_index))
            if self.arr[prob_index] is None:
                return prob_index
            elif self.arr[prob_index][0] == key:
                return prob_index
        raise  Exception("HashMap is full")


ht = HashTable()
ht['march 6'] = 10
ht['march 4'] = 19
ht['march 6'] = 27
ht['march 17'] = 12
print(ht.arr)
print(ht['march 6'])
print(ht['march 4'])
print(ht['march 17'])
print(ht.arr)

