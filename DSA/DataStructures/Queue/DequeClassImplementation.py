from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
            return self.buffer.pop()
    def peek(self):
        self.buffer.pop(-1)

    def isEmpty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def display(self):
        print(self.buffer)


queue = Queue()
queue.enqueue('10')
queue.enqueue('12')
queue.enqueue('19')
queue.enqueue('27')
queue.enqueue('30')
# queue.enqueue({
#     'company': 'Wall Mart',
#     'timestamp': '15 apr, 11.01 AM',
#     'price': 131.10
# })
# queue.enqueue({
#     'company': 'Wall Mart',
#     'timestamp': '15 apr, 11.02 AM',
#     'price': 132
# })
# queue.enqueue({
#     'company': 'Wall Mart',
#     'timestamp': '15 apr, 11.03 AM',
#     'price': 135
# })
queue.display()
print(queue.dequeue())
print(queue.dequeue())
queue.display()
