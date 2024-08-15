from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        return self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def display(self):
        print(self.container)

stack = Stack()
stack.push('siva')
stack.push('balan')
stack.push('sb')
stack.push('sb10')
stack.display()
print(stack.peek())
print(stack.peek())
stack.display()
print(stack.pop())
print(stack.pop())
stack.display()
stack.reverseString('dfsdf')
