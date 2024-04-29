class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    # def __str__(self, level=0):
    #     ret = " " * level + str(self.data)  + "\n"
    #     for child in self.children:
    #         ret += child.__str__(level + 1)
    #         print(ret)
    #     return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode("Drinks")

cold = TreeNode("Cold Drink")
hot = TreeNode("Hot Drink")
tree.addChild(cold)
tree.addChild(hot)

faluda = TreeNode("Faluda")
shake = TreeNode("Shake")
tea = TreeNode("tea")
coffee = TreeNode("Coffee")
cold.addChild(faluda)
cold.addChild(shake)
hot.addChild(tea)
hot.addChild(coffee)

print(tree.data)
for i in tree.children:
    print(i.data)
