class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head =None
        self.tail =None

    def __str__(self):
        current = self.head
        result = ''
        while current is not None:
            result += str(current.data)
            if current.next is not None:
                result += " --> "
            current = current.next
        return result
    
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            if current.data:
                count += 1
            current = current.next
        return count

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def rotate(self, index):
        if index > self.length():
            print("Sorry Index is greater than actual LinkedList")
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            if current.next:
                if current != self.tail:
                    self.tail.next = self.head
                    self.tail = current
                    self.head = current.next
                    self.tail.next =None

    def reverse(self):
        if self.head == self.tail:
            print("Only one node is present")
        else:
            if self.head.next:
                self.tail = self.head
                self.head = self.tail.next
                self.tail.next = None
                prev = self.tail
            
            
        while self.head.next is not None:
            next_node = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = next_node
        self.head.next = prev

    def remove(self, value):

        current = self.head
        prev = self.head
        while current.next is not None:
            if self.head == current and self.head.data == value:
                self.head = self.head.next
                break
            elif current.data == value:
                prev.next = current.next
                break
            else:
                prev = current
                current = current.next

    def removeDuplicates(self):
        unique = set()
        prev = Node(-1)
        prev.next = self.head
        curent = self.head
        while curent is not None:
            if curent.data not in unique:
                unique.add(curent.data)
                prev = curent
                curent = curent.next
            else:
                prev.next = curent.next
                curent = curent.next


            

linkedList = LinkedList()
list_items = [10,10, 20, 30, 30, 40, 50, 60, 70, 80, 80, 90, 90, 90, 10]
for item in list_items:
    linkedList.append(item)
print(linkedList)

print(f"Length of LinkedList is {linkedList.length()}")
length = linkedList.length()//2

linkedList.rotate(length)
print(linkedList)

linkedList.rotate(length)
print(linkedList)

linkedList.reverse()
print(linkedList)

linkedList.reverse()
print(linkedList)

linkedList.remove(90)
print(linkedList)

linkedList.removeDuplicates()
print(linkedList)
