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

    def printList(self):
        # print("\nPrinting List...")
        if self.head is None:
            print("LinkedList is empty...")
            return
        itr = self.head
        while itr:
            # print(f"{itr.data}---> {itr}")
            print(itr.data, "---> ")
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtBeginning(10)
    ll.insertAtBeginning(12)
    ll.insertAtBeginning(30)
    ll.printList()
