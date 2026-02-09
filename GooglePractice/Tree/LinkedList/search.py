# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    ## DFS
   
    def search(self, root, target):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        def inorder(root, target):
            if not root:
                return
            
            if inorder(root.left, target):
                return True
            if root.val == target:
                return True
            return inorder(root.right, target)
        return inorder(root, target)

    
drinks = TreeNode("Drinks")
cold = TreeNode("Cold")
hot = TreeNode("Hot")
drinks.left = cold
drinks.right = hot
coffee = TreeNode("coffee")
coke = TreeNode("coke")
cold.left = coffee
cold.right = coke

print(Solution().search(drinks, "cke"))



        