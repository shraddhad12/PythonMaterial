class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    # def __str__(self):
    #     return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

class CustomQueue:
    def __init__(self):
        self.list = LinkedList()

    def __str__(self):
        items = [str(i.value) for i in self.list]
        return " ".join(items)
    
    def isEmpty(self):
        if self.list.head == None:
            return True
        else:
            return False
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.list.head = new_node
            self.list.tail = new_node
        else:
            self.list.tail.next = new_node
            self.list.tail = new_node

    def dequeue(self):
        if self.isEmpty():
            print("No items in Queue")
        else:
            self.list.head = self.list.head.next

    def peek(self):
        if self.isEmpty():
            return "No items in Queue"
        else:
            return self.list.head.value
            

    def delete(self):
        self.list.head = None
        self.list.tail = None


queue = CustomQueue()
print(queue.isEmpty())

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
print(queue)

queue.dequeue()
print(queue)

print(queue.peek())

print("after deletion", queue.delete())

