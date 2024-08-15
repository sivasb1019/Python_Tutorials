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
        # print("LinkedList class(insert) ---> head:", self.head, "data:", self.head.data)

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insertUsingList(self, fruits):
        for fruit in fruits:
                self.insertAtEnd(fruit)

    def insertAtPosition(self, index, data):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid Index!!!")

        if index == 0:
            self.insertAtBeginning(data)
            return

        itr = self.head
        count = 1
        while itr:
            if count == index:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count  += 1


    def removeAtPosition(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid Index!!!")

        if index == 0:
            self.head = self.head.next
            return

        count = 1
        itr = self.head
        while itr:
            if count == index:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1


    def insertAfterValue(self, afterData, data):
        if self.head is None:
            return

        itr = self.head
        while itr:
            if afterData == itr.data:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next

    def removeByValue(self, data):
        if self.head is None:
            return

        itr = self.head
        while itr:
            if itr.data == data:
                # print("\n\n",itr, itr.next)
                if itr == self.head:
                    self.head = itr.next
                else:
                    itr.next = itr.next.next
                break
            itr = itr.next

    def printList(self):
        print()
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
        itr = self.head
        while itr:
            length+=1
            itr = itr.next
        return length

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertUsingList(["banana", "apple", "orange", "mango",
                        "grape", "cherry", "pineapple"])
    ll.printList()
    print("\nLength of the LinkedList: ", ll.getLength())
    ll.removeAtPosition(2)
    ll.printList()
    ll.insertAtPosition(0, "green apple")
    ll.printList()
    ll.insertAtPosition(2, "dragon fruit")
    ll.printList()
    ll.insertAfterValue("mango", "jackfruit")
    # ll.insertAtPosition(2, "dragon fruit")
    ll.printList()
    ll.removeByValue("green apple")
    ll.printList()
    print("\nLength of the LinkedList: ", ll.getLength())
