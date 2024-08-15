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


def reverseString( value):
    stack = Stack()
    for char in value:
        stack.push(char)
    reverseValue = ''
    while stack.size() != 0:
        reverseValue += stack.pop()
    return reverseValue


if __name__ == '__main__':
    print(reverseString('We will conquere COVID-19'))
    print(reverseString("I am the king"))