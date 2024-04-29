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

def postOrderTraversal(rootNode):
    if not rootNode:
        return ''
    postOrderTraversal(rootNode.leftNode)
    postOrderTraversal(rootNode.rightNode)
    print(rootNode.data)
    

postOrderTraversal(newBT)