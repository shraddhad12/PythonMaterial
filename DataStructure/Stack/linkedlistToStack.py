class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

class CustomStack:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        if self.isEmpty():
            return ""
        else:
            values = [str(i.value) for i in self.linkedlist]
            return "\n".join(values)
    
    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False
        
    def push(self, value):

        ## Need to Understand
        new_node = Node(value)
        new_node.next = self.linkedlist.head
        self.linkedlist.head = new_node

    def pop(self):
        if self.isEmpty():
            return "No elements present"
        else:
            popped_node = self.linkedlist.head.value
            self.linkedlist.head = self.linkedlist.head.next
            return popped_node
        
    def peek(self):
        if self.isEmpty():
            return "No elements present"
        else:
            node = self.linkedlist.head.value
            return node
        
    def delete(self):
        self.linkedlist.head = None

cs = CustomStack()
cs.push(10)
cs.push(20)
cs.push(30)
cs.push(40)

print("popped element", cs.pop())
print(cs)

print("peek top element from stack", cs.peek())

cs.delete()
print("after stack deletion", cs)