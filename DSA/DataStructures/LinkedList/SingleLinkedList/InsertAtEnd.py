class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        # print(f"Node class ---> data: {data} | next: {next}\n" )


class LinkedList:
    def __init__(self):
        self.head = None
        # print("LinkedList class(init) ---> head:", self.head)

    def insertAtEnd(self, data):
        if self.head is None:
            # print(self.head, data)
            self.head = Node(data, None)
            # print(self.head, data)
            return
        itr = self.head
        while itr.next:
            # print(itr, itr.data)
            itr = itr.next
            # print(itr, itr.data)
        itr.next = Node(data, None)
    def printList(self):
        # print("\nPrinting List...")
        if self.head is None:
            print("LinkedList is empty...")
            return
        itr = self.head
        while itr:
            # print(f"{itr.data}---> {itr}")
            print(itr.data, end="---> ")
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtEnd(10)
    ll.insertAtEnd(12)
    ll.insertAtEnd(30)
    ll.printList()
