class Node:
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next

class Solution:
    def search(self, head, target):
        if not head:
            return False
        current = head
        while current:
            if current.val == target:
                return True
            current = current.next
        return False
    
head = Node(5, Node(4, Node(3, Node(2, Node(1)))))
print(Solution().search(head, -2))


