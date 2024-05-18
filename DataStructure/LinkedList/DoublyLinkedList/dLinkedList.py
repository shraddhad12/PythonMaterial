class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        result = ''
        current = self.head
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += " <==> "
            current = current.next
        return result


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def verify(self):
        if self.head is None:
            print("No node present")
        elif self.head == self.tail:
            print(self.head.value)
        else:
            node = self.tail.prev
            print(f"{node.value}")

    def reverse(self):
        result = ''
        current = self.tail
        while current is not None:
            result += str(current.value)
            if current.prev is not None:
                result += " <==> "
            current = current.prev
        return result
            

dlinkedlist = DLinkedList()
dlinkedlist.append(10)
dlinkedlist.append(20)
dlinkedlist.append(30)
dlinkedlist.append(40)
dlinkedlist.append(50)
dlinkedlist.append(60)
dlinkedlist.append(70)

print(dlinkedlist)

dlinkedlist.verify()

print(dlinkedlist.reverse())
# print(dlinkedlist)