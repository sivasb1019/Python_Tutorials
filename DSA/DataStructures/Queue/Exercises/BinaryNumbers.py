from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is EMpty")
            return
        return self.buffer.pop()

    def isEmpty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

    def display(self):
        print(self.buffer)
def produceBinaryNo(limit):
    numbersQueue = Queue()
    numbersQueue.enqueue('1')
    for i in range(limit):
        numbersQueue.display()
        front = numbersQueue.front()
        print("  ", front)
        numbersQueue.enqueue(front + '0')
        numbersQueue.enqueue(front + "1")
        numbersQueue.dequeue()


limit = int(input("Enter limit: "))
produceBinaryNo(limit)
