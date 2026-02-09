# Define TreeNode class (unless interviewer provides it)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Implement Binary Search Tree Search
def search_BST(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    elif target < root.val:
        return search_BST(root.left, target)
    else:
        return search_BST(root.right, target)
    
def valid_bst(root):
    def valid(root, left, right):
        if not root:
            return True
        if not (left < root.val < right):
            return False
        return valid(root.left, left, root.val) and valid(root.right, root.val, right)
    return valid(root, float("-inf"), float("inf"))

def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if root.val > val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

def traversal(root):
    new = []
    def traverse(root):
        if not root:
            return
        new.append(root.val)
        traverse(root.left)
        traverse(root.right)
    traverse(root)
    return new


# Example usage
root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8))
print(search_BST(root, 4))

root = insert_bst(root, 10)

print(valid_bst(root))

print(traversal(root))