import collections

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Function to build a test graph
def build_test_graph():
    """
    Creates the following undirected graph:
    
        1 -- 2
        |    |
        4 -- 3

    Returns the reference to node 1.
    """
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    return node1  # Return reference to the first node

## BFS

def bfs_traversal(node1):
    queue = collections.deque([node1])
    visited = set()
    visited.add(node1.val)
    while queue:
        current_vertex = queue.popleft()
        for other_vertex in current_vertex.neighbors:
            if other_vertex.val not in visited:
                visited.add(other_vertex.val)
                queue.append(other_vertex)
    return visited

def dfs_traversal(node1):
    stack = [node1]
    visited = set()
    visited.add(node1.val)
    while stack:
        current_vertex = stack.pop()
        if current_vertex.val not in visited:
            visited.add(current_vertex.val)
        for other_vertex in current_vertex.neighbors:
            if other_vertex.val not in visited:
                stack.append(other_vertex)
    return visited


node1 = build_test_graph()
print(bfs_traversal(node1))
print(dfs_traversal(node1))

