class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        # print(f"{self.data} ---> {self.next} ---> {self.prev}\n")


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,data):
        if self.head is None:
            self.head = Node(data,self.head, None)
        else:
            # node = Node(data, self.head, None)
            # self.head.prev = node
            # self.head = node
            self.head = Node(data, self.head, None)
            self.head.next.prev  = self.head

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, self.head, None)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None, itr)

    def insertUsingList(self, datas):
        for data in datas:
            self.insertAtBeginning(data)

    def insertAtPosition(self, index, data):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid Index")

        if index == 0:
            self.insertAtBeginning(data)
        else:
            count = 1
            itr = self.head
            while itr:
                if count == index:
                    itr.next = Node(data, itr.next, itr)
                    itr.next.next.prev = itr.next
                    # print(itr.next.next.prev, itr.next)
                    break
                itr = itr.next
                count += 1

    def removeAtPosition(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            count = 1
            itr = self.head
            while itr:
                if count == index:
                    itr.next = itr.next.next
                    itr.next.prev = itr
                itr = itr.next
                count += 1

    def insertByValue(self, afterdata, data):
        if self.head is None:
            print("Linked List is empty...")
            return

        present = False
        itr = self.head
        while itr:
            if itr.data == afterdata:
                itr.next = Node(data, itr.next, itr)
                itr.next.next.prev = itr.next
                present = True
                break
            itr = itr.next
        if not present:
            print(f"{afterdata} is not in presented in the LinkedList")

    def removeByValue(self, data):
        if self.head is None:
            print("Linked List is empty...")
            return

        present = False

        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head.next
        while itr:
            if itr.data == data:
                itr.next.prev = itr.prev
                itr.prev.next = itr.next
                present = True
            itr = itr.next
        if not present:
            print(f"{data} is not in the LinkeList")

    def printForward(self):
        print()
        if self.head is None:
            print("Linked List is empty...")
            return
        itr = self.head
        while itr:
            # print(f"{itr.data} ---> {itr.next} ---> {itr.prev}")
            print(itr.data, end = " ---> ")
            itr = itr.next

    def printBackward(self):
        print()
        if self.head is None:
            print("Linked List is Empty...")
            return
        itr = self.getLastNode()
        while itr:
            # print(f"{itr.data} ---> {itr.next} ---> {itr.prev}")
            print(itr.data, end=" ---> ")
            itr = itr.prev

    def getLastNode(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def getLength(self):
        itr = self.head
        length = 0
        while itr:
            length += 1
            itr = itr.next
        return length

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtBeginning("banana")
    ll.insertAtEnd("apple")
    ll.insertAtBeginning("orange")
    ll.insertUsingList(["mango", "grape", "cherry", "pineapple"])
    ll.printForward()
    ll.printBackward()
    print("Inserting data by position:")
    ll.insertAtPosition(1, "jack fruit")
    ll.printForward()
    ll.printBackward()
    print("\nRemoving data by position:")
    ll.removeAtPosition(2)
    ll.printForward()
    ll.printBackward()
    print("\nInserting data by Value:")
    ll.insertByValue("cherry", "grape")
    ll.printForward()
    ll.printBackward()
    print("\nRemoving data by Value:")
    ll.removeByValue("pineapple")
    ll.printForward()
    ll.printBackward()



