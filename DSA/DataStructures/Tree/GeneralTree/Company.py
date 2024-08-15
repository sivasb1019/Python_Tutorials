class TreeNode:
    def __init__(self, name, role):
        self.data = (name, role)
        # self.role = role
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
        spaces = " "*self.getLevel() * 2
        prefix = spaces + "|__" if self.parent else ""
        if value == "name":
            print(prefix, self.data[0])
        if value == "designation" or value == "role":
            print(prefix, self.data[1])
        if value == "both":
            print(prefix, self.data[0], f"({self.data[1]})")
        if self.children:
            for child in self.children:
                child.displayTree(value)


def buildTreeNode():
    root = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay", "CTO")
    infra_head = TreeNode("Vishwa", "Insfrastructure Head")
    infra_head.addChild(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.addChild(TreeNode("Abhijit", "App Manager"))
    app_head = TreeNode("Aamir", "Application Head")
    cto.addChild(infra_head)
    cto.addChild(app_head)

    hr_head = TreeNode("Gels", "HR Head")
    hr_head.addChild(TreeNode("Peter", "Recruitment Manager"))
    hr_head.addChild(TreeNode("Waqas", "Policy Manager"))

    root.addChild(cto)
    root.addChild(hr_head)

    return root


if __name__ == '__main__':
    root = buildTreeNode()
    root.displayTree("both")