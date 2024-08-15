from collections import deque

queue = deque()
queue.appendleft(10)
queue.appendleft(12)
queue.appendleft(19)
queue.appendleft(27)
queue.appendleft(30)
print(queue)
print(queue.pop())
print(queue.pop())
print(queue)
