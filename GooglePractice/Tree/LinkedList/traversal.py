import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    ## DFS
   
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        newList = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)    # --------------------O(n/2)
            newList.append(root.val) # -----------------O(1)
            inorder(root.right)   # --------------------O(n/2)
        inorder(root)
        return newList
    
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

    def postorderTraversal(self, root):
        newList = []
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            newList.append(root.val)
        postorder(root)
        return newList
    
    ## BFS

    def levelorderTraversal(self, root):
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            level = []
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
    
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        q = collections.deque()
        q.append(root)
        result = []
        while q:
            qlen = len(q)
            level = []
            for _ in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.insert(0, level)
        return result
    
    
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
     
        q = collections.deque()
        q.append(root)
        dict = {}
        level = 0
        while q:
            qLen = len(q)
            sum = 0
            level += 1
            for i in range(qLen):
                node = q.popleft()
                sum += node.val
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            dict[level] = sum
        return max(dict, key = dict.get)
    


# drinks = TreeNode("Drinks")
# cold = TreeNode("Cold")
# hot = TreeNode("Hot")
# drinks.left = cold
# drinks.right = hot
# coffee = TreeNode("coffee")
# coke = TreeNode("coke")
# cold.left = coffee
# cold.right = coke
    


root = TreeNode(10, TreeNode(20, None, TreeNode(5)), TreeNode(30, TreeNode(40), TreeNode(50)))

# print(Solution().levelorderTraversal(root))

# print(Solution().maxLevelSum(root))

# dict = {1:-1,2: 0, 3: 0}
# print(max(dict, key = dict.get))

print(Solution().preorderTraversal(root))



        