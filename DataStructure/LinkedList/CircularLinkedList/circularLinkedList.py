class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        result = ''
        current = self.head
        while current is not None:
            result += str(current.value)
            current = current.next
            if current is self.head:
                break
            result += " --> "
           
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

clinkedlist = CLinkedList()
clinkedlist.append(10)
clinkedlist.append(20)
clinkedlist.append(30)
clinkedlist.append(40)
clinkedlist.append(50)
clinkedlist.append(60)

print(clinkedlist)