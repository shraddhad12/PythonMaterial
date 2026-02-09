class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList(object):

    def __init__(self) -> None:
        self.head = None
        self.tail =None

    def __str__(self) -> str:
        result = ''
        current = self.head
        while current is not None:
            result += str(current.val)
            if current.next is not None:
                result += " --> "
            current = current.next
        return result
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def create(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

class CustomQueue:
    def __init__(self) -> None:
        self.linkedlist = LinkedList()

    def __str__(self) -> str:
        values = [str(i.val) for i in self.linkedlist]
        return " ".join(values)
        
    def enque(self, value):
        new = Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head = new
            self.linkedlist.tail = new
        else:
            self.linkedlist.tail.next = new
            self.linkedlist.tail = new           

queue = CustomQueue()
queue.enque(10)
queue.enque(20)
queue.enque(30)
queue.enque(40)

print(queue)
        
    
