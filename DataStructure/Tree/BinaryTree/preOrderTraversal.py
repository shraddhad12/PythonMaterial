class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

newBT = TreeNode("Drinks")
hot =TreeNode("Hot")
cold = TreeNode("Cold")
newBT.leftNode = cold
newBT.rightNode = hot

coffee =TreeNode("Coffee")
tea = TreeNode("Tea")
hot.leftNode = coffee
hot.rightNode = tea

shake =TreeNode("Shake")
faluda = TreeNode("Faluda")
cold.leftNode = shake
cold.rightNode = faluda

chochlate = TreeNode("Chochlate")
shake.leftNode = chochlate

def preOrderTraversal(rootNode):
    if not rootNode:
        return ''
    print(rootNode.data)
    preOrderTraversal(rootNode.leftNode)
    preOrderTraversal(rootNode.rightNode)

preOrderTraversal(newBT)