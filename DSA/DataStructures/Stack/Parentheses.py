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

def isMatch(cp, op):
    bracket_dict = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }
    return  bracket_dict[cp] == op


def isBalanced( value):
    stack = Stack()
    for char in value:
        if char=='(' or char=='[' or char=='{':
            stack.push(char)
        if char == ')' or char == ']' or char == '}':
            if stack.size()==0:
                return  False
            if not isMatch(char, stack.pop()):
                    return False
    return stack.size()==0


if __name__ == '__main__':
    print(isBalanced("({a+b})"))
    print(isBalanced("))((a+b}{"))
    print(isBalanced("((a+b))"))
    print(isBalanced("))"))
    print(isBalanced("[a+b]*(x+2y)*{gg+kk}"))