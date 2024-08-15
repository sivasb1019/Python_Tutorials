class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, child):
        if child == self.data:
            return

        if child < self.data:
            # Add child in left subtree
            if self.left:
                self.left.addChild(child)
            else:
                self.left = BinarySearchTreeNode(child)
        else:
            # Add child in right subtree
            if self.right:
                self.right.addChild(child)
            else:
                self.right = BinarySearchTreeNode(child)

    def searchElement(self, value):
        if value == self.data:
            return True
        if value < self.data:
            # Value might be in left subtree
            if self.left:
                return self.left.searchElement(value)
            else:
                return False
        if value > self.data:
            # Value might be in right subtree
            if self.right:
                return self.right.searchElement(value)
            else:
                return False

    def maximumElement(self):
        if self.right:
            return self.right.maximumElement()
        return self.data

    def minimumElement(self):
        if self.left:
            return self.left.minimumElement()
        return self.data

    def deleteElement(self, value):
        if value < self.data:
            if self.left:
                self.left.deleteElement(value)
        elif value > self.data:
            if self.right:
                self.right.deleteElement(value)
        else:
            if self.left is None and self.right is None:
                return  None
            if self.left is None:
                return  self.right
            if self.right is None:
                return  self.left
            min_value = self.right.minimumElement()
            self.data = min_value
            self.right = self.deleteElement(min_value)
        return  self


def buildBinarySearchTree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in  range(1, len(elements)):
        root.addChild(elements[i])
    return  root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20,  9, 23, 18, 34]
    # numbers = [15, 12,27,14, 7, 88,20,23]

    numbersTree = buildBinarySearchTree(numbers)
    print(numbersTree.maximumElement())
    print(numbersTree.minimumElement())
    print(numbersTree.deleteElement(9))

