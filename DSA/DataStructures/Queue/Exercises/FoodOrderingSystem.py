import time
from collections import deque
from threading import Thread


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


queue = Queue()


def placeOrder(orders):
    for food in orders:
        print("Placing order for", food)
        queue.enqueue(food)
        time.sleep(0.5)


def serveOrder():
    time.sleep(1)
    while not queue.isEmpty():
        print("Now Serving:", queue.dequeue())
        time.sleep(2)


orders = ['pizza','samosa','pasta','biryani','burger']
t1 = Thread(target=placeOrder, args=(orders,))
t2 = Thread(target=serveOrder)

t1.start()
t2.start()

t1.join()
t2.join()

