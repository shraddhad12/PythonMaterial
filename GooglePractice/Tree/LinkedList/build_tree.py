import collections


class TreeNode:
    def __init__(self, value, left = None, right=None) -> None:
        self.val = value
        self.left = left
        self.right = right

class tree:

    def create(self, tree1):
        root = TreeNode(tree1[0])
        stack = [root]
        i = 1

        while i < len(tree1):
            node = stack[-1]
            if not tree1:
                return
            if tree1[i] is not None:
                newNode = TreeNode(tree1[i])
                if not node.left:
                    node.left = newNode
                else:
                    node.right = newNode
                    stack.pop()
                stack.append(newNode)
            else:
                if node.left:
                    stack.pop()
            i += 1
        return root

    def preorderTraversal(self, root):
        newList = []
        def preorder(root):
            if not root:
                return
            newList.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return newList


    # def buildTree(self, preorder, inorder):
    #     if inorder:
    #         INDEX = inorder.index(preorder.pop(0))
    #         print(INDEX)
    #         root = TreeNode(inorder[INDEX])
    #         root.left = self.buildTree(preorder, inorder[:INDEX])
    #         root.right = self.buildTree(preorder, inorder[INDEX+1:])
			
    #         return root




preorder = [3,9,None,None,20,15,7]
inorder = [9,3,15,20,7]
root = tree().create(preorder)
# print(tree().preorderTraversal(root))

