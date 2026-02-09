# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def traversal(self, head: ListNode):
        if head is not None:
            result = ""
            while head is not None:
                result += str(head.val)
                if head.next is not None:
                    result += " --> "
                head = head.next
            return result
        else:
            return None

    def create(self, list):
        head = None
        tail = None
        for i in list:
            newNode = ListNode(val=i)   
            if head is None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
        return head


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode() 
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
        return dummy.next
    
    def removeNthFromEnd(self, head: ListNode, n):
        dummy = head
        length = 0
        
        while dummy is not None:
            dummy = dummy.next
            length += 1
        if length == 0:
            return None
        if length == n:
            return head.next
        dummy = head
        for _ in range(1, length - n):
            dummy = dummy.next
        dummy.next = dummy.next.next
        return head
    

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ptr, length = head, 0
        while ptr:
            ptr, length = ptr.next, length + 1
        if length == n : return head.next
        ptr = head
        for i in range(1, length - n):
            ptr = ptr.next
        ptr.next = ptr.next.next
        return head
    
    def merge(self, left, right):
        dummy = ListNode(0)
        newList = dummy
        while left and right:
            if left.val < right.val:
                newList.next = left
                left = left.next
            else:
                newList.next = right
                right = right.next
            newList = newList.next
        newList.next = left or right
        return dummy.next

    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists)//2
        l_half = lists[:mid]
        r_half = lists[mid:]
        l_half = self.mergeKLists(l_half)
        r_half = self.mergeKLists(r_half)
        return self.merge(l_half, r_half)

linkedList = Solution()
# l1 = linkedList.create([1,7])
# l2 = linkedList.create([5,6,4])
# print(linkedList.traversal(l1))
# print(linkedList.traversal(l2))
# l3 = Solution().addTwoNumbers(l1, l2)

# print()
# print(linkedList.traversal(l3))

# head = Solution().removeNthFromEnd(l1,2)
# print(linkedList.traversal(head))

lists = [[1,4,5],[1,3,4],[2,6]]
list_nodes = []
for i in lists:
    list_nodes.append(linkedList.create(i))

result = Solution().mergeKLists(list_nodes)
print(linkedList.traversal(result))



