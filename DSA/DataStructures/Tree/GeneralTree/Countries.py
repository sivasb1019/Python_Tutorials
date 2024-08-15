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

    def displayTree(self, value):
        if self.getLevel() > value:
            return
        spaces = " " * self.getLevel() * 2
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.displayTree(value)


def buildProductTree():
    root = TreeNode("Global")

    country1 = TreeNode("India")
    state1 = TreeNode( "Gujarat")
    state1.addChild(TreeNode("Ahmedabad"))
    state1.addChild(TreeNode("Baroda"))
    state2 = TreeNode( "Karnataka")
    state2.addChild(TreeNode("Bengaluru"))
    state2.addChild(TreeNode("Mysore"))

    country1.addChild(state1)
    country1.addChild(state2)

    country2 = TreeNode("USA")
    state1 = TreeNode("New Jersey")
    state1.addChild(TreeNode("Princeton"))
    state1.addChild(TreeNode("Trenton"))
    state2 = TreeNode("California")
    state2.addChild(TreeNode("San Francisco"))
    state2.addChild(TreeNode("Mountain View"))
    state2.addChild(TreeNode("Palo ALto"))

    country2.addChild(state1)
    country2.addChild(state2)

    root.addChild(country1)
    root.addChild(country2)

    return root


if __name__ == '__main__':
    root = buildProductTree()
    root.displayTree(2)
