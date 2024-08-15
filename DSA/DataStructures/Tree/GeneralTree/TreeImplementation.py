class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def displayTree(self):
        spaces = " " * self.getLevel() * 2
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.displayTree()


def buildProductTree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.addChild(TreeNode("HP pavilion"))
    laptop.addChild(TreeNode("MacBook"))
    laptop.addChild(TreeNode("Asus"))

    tv = TreeNode("Television")
    tv.addChild(TreeNode("LG"))
    tv.addChild(TreeNode("Samsung"))
    tv.addChild(TreeNode("Sony"))

    mobile = TreeNode("Mobiles")
    mobile.addChild(TreeNode("Redmi Note 9"))
    mobile.addChild(TreeNode("Iphone"))
    mobile.addChild(TreeNode("Google Pixel"))

    root.addChild(laptop)
    root.addChild(tv)
    root.addChild(mobile)

    return root


if __name__ == '__main__':
    root = buildProductTree()
    root.displayTree()
    pass