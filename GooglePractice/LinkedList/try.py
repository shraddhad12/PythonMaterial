class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data)
            if current.next is not None:
                result += " --> " 
            current = current.next
        return result

    def get_length(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length

    
    def append_at_end(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def get(self, index):
        if index < 0:
            return "No node available"
        current = self.head
        for _ in range(index):
            current = current.next
        if current.data is not None:
            return f"{current.data} is present at index {index}"
        return f"No Node present at index {index}"
    
        
    def set(self, value, index):
        if index > self.get_length():
            print("Index is greater than List")
        else:
            newNode = Node(value)
            if self.head and self.tail:
                if index == -1:
                    self.tail.next = newNode
                    self.tail = newNode
                elif index == 0:
                    newNode.next = self.head
                    self.head = newNode
                elif index > 0:
                    current = self.head
                    for _ in range(index-1):
                        current = current.next
                    if current is not None:
                        # newNode.next = current.next
                        # current.next = newNode 
                        newNode.next  = current.next
                        current.next = newNode
                    else:
                        print(f"Index {index} is greater than length of LinkedList")
                else:
                    print(f"Index {index} is less than length of LinkedList")
            else:
                self.head = newNode
                self.tail = newNode


    def pop_first(self):
        if self.head is None:
            return "No element present in linkedlist"
        popped_node = self.head
        if self.head == self.tail:
            self.tail = None
            self.head = None
        self.head = self.head.next
        return popped_node.data

    def reverse_list(self):
        if self.head.next:
            self.tail = self.head
            self.head = self.head.next
            self.tail.next = None
            prev = self.tail
        
        while self.head.next is not None:
            next_node = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = next_node
        self.head.next = prev

                       
l1 = LinkedList()
for i in range(10):
    l1.append_at_end(i)

# print(l1.get_length())

l1.prepend(100)
print(l1)

print(l1.get(3))

l1.set(10, 0)
l1.set(20, 1)
print(l1)

print(l1.pop_first())
print(l1)

l1.reverse_list()
print(l1)

    