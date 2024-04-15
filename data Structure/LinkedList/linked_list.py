#Initiale Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Creating Node
nodes = []
for i in range(10):
    nodes.append(Node(i))
    if i > 1 or i < 100:
        nodes[i-1].next = nodes[i]

#Connecting nodes
# for n in range(len(nodes)-1):
#     nodes[n].next = nodes[n+1]

#printing the linkedList
current = nodes[0]
while current is not None:
    result = str(current.data)
    print(result, end=" --> ") if current.next is not None else print(result)
    print((current), (current.next))
    print(type(current), type(current.next))
    current = current.next


