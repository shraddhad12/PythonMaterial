#Initiale Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None
current = None


def append(new_node, current):
    current.next = new_node


for i in range(10):
    if i < 1:
        head = Node(i)
        current = head
        new_node = Node(i+1)
        append(new_node, current)
        current = new_node
    elif current.next is None:
        new_node = Node(i+1)
        append(new_node, current)
        current = new_node
current.next = None


#printing the linkedList
current = head
while current is not None:
    result = str(current.data)
    print(result, end=" --> ") if current.next is not None else print(result)
    current = current.next


