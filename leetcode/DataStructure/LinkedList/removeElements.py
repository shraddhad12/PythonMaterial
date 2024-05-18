class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        dummy_head = ListNode(-1)
        dummy_head.next = head
        current = head
        prev = dummy_head
        while current is not None:
            if current.val == val:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        return dummy_head.next

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """ 
        if head is not None and head.next is not None:
            prev = head
            head = prev.next
            prev.next = None
            while head.next is not None:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            head.next = prev
            return head
        return head
    
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is not None:
            current = head
            count = 0
            while current is not None:
                if current.val:
                    count += 1
                current = current.next
            index = count//2
            if count > 1:
                middle_node = head
                for _ in range(index):
                    middle_node = middle_node.next
                return middle_node
            else:
                return head
        else:
            return head
    
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(-1)
        prev = dummy_head
        while list1 and list2:
            if list1.val > list2.val:
                prev.next = list2
                list2 = list2.next
            else:
                prev.next = list1
                list1 = list1.next
            prev = prev.next
        prev.next = list1 if list1 is not None else list2
        return dummy_head.next
    
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(-1)
        prev = dummy_head
        prev.next = head
        current = head
        unique = set()
        while current is not None:
            if current.val not in unique:
                unique.add(current.val)
                prev = current
                current = current.next
            else:
                prev.next = current.next
                current = current.next
        return dummy_head.next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        current_node = self.head
        result = ''
        while current_node is not None:
            result += str(current_node.val)
            if current_node.next is not None:
                result += " --> "
            current_node = current_node.next
        return result

    def append(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self):
        self.head =  Solution().removeElements(self.head, 6)
    def reverse(self):
        self.head = Solution().reverseList(self.head)
    def middleNode(self):
        return Solution().middleNode(self.head)
    def merge(self):
        l1 = LinkedList()
        ls = [1,3, 6]
        for i in ls:
            l1.append(i)

        l2 = LinkedList()
        ls = [1, 2, 2,4,5,6]
        for i in ls:
            l2.append(i)
        
        self.head = Solution().mergeTwoLists(l1.head, l2.head)

    def removeDuplicates(self):
        Solution().deleteDuplicates(self.head)


linkedList = LinkedList()
head = [1,2,6,3,4,5,6]
for i in head:
    linkedList.append(i)

    
linkedList.remove()
linkedList.reverse()

print(linkedList)
print("Middle Node of a LinkedList", linkedList.middleNode().val)


linkedList.merge()
print(linkedList)

linkedList.removeDuplicates()
print(linkedList)