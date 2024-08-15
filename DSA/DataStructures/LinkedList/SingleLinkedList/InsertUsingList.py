class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        # print(f"Node class ---> data: {data} | next: {next}\n" )


class LinkedList:
    def __init__(self):
        self.head = None
        # print("LinkedList class(init) ---> head:", self.head)

    def insertAtBeginning(self, data):
        self.head = Node(data, self.head)
        # print("LinkedList class(insert) ---> head:", self.head)

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insertUsingList(self, fruits):
        if self.head is None:
            for fruit in fruits:
                self.insertAtBeginning(fruit)
        else:
            for fruit in fruits:
                self.insertAtEnd(fruit)

    def printList(self):
        # print("\nPrinting List...")
        if self.head is None:
            print("LinkedList is empty...")
            return
        itr = self.head
        while itr:
            # print(f"{itr.data}---> {itr}")
            print(itr.data, end=" ---> ")
            itr = itr.next

    def getLength(self):
        length = 0
        while self.head:
            length+=1
            self.head = self.head.next
        return length

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertUsingList(["banana", "apple", "orange", "mango"])
    ll.insertUsingList(["grape", "cherry", "pineapple"])
    ll.printList()
    print("\nLength of the LinkedList: ", ll.getLength())
