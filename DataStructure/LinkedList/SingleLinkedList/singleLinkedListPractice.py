class Node:
    def __init__(self, value):
        self.value = value
        self.next =None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        current_node = self.head
        result = ''
        while current_node is not None:
            result += str(current_node.value)
            if current_node.next is not None:
                result += " --> "
            current_node = current_node.next
        return result

    
    def create_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def traverseLinkedList(self):
        current_node = self.head
        result = ''
        while current_node is not None:
            result += str(current_node.value)
            if current_node.next is not None:
                result += " --> "
            current_node = current_node.next
        return result
    
    def prepand(self, value):
        new_node = Node(value)
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail  = new_node

    def get_node(self, index):
        if index == 0:
            return self.head
        elif index == -1:
            return self.tail
        else:
            current = self.head
            for _ in range(index):
                if current.next is None:
                    return None
                current = current.next
                
            if current.value is not None:
                return current
            else:
                return None
            
    def set_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            if self.head is not None:
                new_node.next = self.head
                self.head = new_node
            else:
                self.head = new_node
                self.tail = new_node
        elif index == -1:
            if self.tail is not None:
                self.tail.next = new_node
                self.tail = new_node
            else:
                self.head = new_node
                self.tail = new_node
        else:
            current = self.head
            for _ in range(index-1):
                if current.next is None:
                    print(f"No index {index} present in linkedList")
                    break
                current = current.next
            if current.value is not None:
                new_node.next = current.next
                current.next = new_node
            else:
                print(f"No index {index} present in linkedList")


    def reverse_linkedList(self):
        if self.head == self.tail and self.head is None:
            print("only one node is present")
        else:
            if self.head.next is not None:
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

    def pop_last(self):
        if self.head == self.tail:
            self.head =None
            self.tail =None
        else:
            popped_node = self.tail
            current = self.head
            while current.next is not self.tail:
                current = current.next
            self.tail = current
            current.next = None
            print(f"Popped last element {popped_node.value}")
            popped_node.value = None

    def pop_first(self):
        if self.head == self.tail:
            self.head =None
            self.tail = None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.value = None

    def remove(self, value):

        current = self.head
        prev = self.head
        while current.next is not None:
            if self.head == current and self.head.value == value:
                self.head = self.head.next
                break
            elif current.value == value:
                prev.next = current.next
                break
            else:
                prev = current
                current = current.next
            

linkedlist = LinkedList()
for i in range(10, 100, 10):
    linkedlist.create_node(i)
print(linkedlist)

linkedlist.prepand(101)
linkedlist.prepand(102)
print(linkedlist)

index = 6
node = linkedlist.get_node(index)
if node is not None:
    print(f"{node.value} is at index {index}")
else:
    print(f"No node present at index {index}")

linkedlist.set_node(6, 103)
print(linkedlist.traverseLinkedList())

linkedlist.pop_last()
print(linkedlist)

linkedlist.pop_first()
print(linkedlist)

linkedlist.reverse_linkedList()
print(linkedlist)

linkedlist.remove(20)
print(linkedlist)

print(linkedlist.traverseLinkedList())

