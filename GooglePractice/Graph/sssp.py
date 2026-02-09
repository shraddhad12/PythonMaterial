class Node:
    def __init__(self, val,neighbours = None) -> None:
        self.val = val
        self.neighbours = neighbours if neighbours is not None else []

class Graph:
    def sssp_bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop()
            current_node = path[-1]
            if current_node.val == end.val:
                return path
            for other_vertices in current_node.neighbours:
                new_path = list(path)
                new_path.append(other_vertices)
                queue.append(new_path)


node1 = Node("a")
node2 = Node("b")
node3 = Node("c")
node4 = Node("d")
node5 = Node("e")
node6 = Node("f")
node7 = Node("g")
             
node1.neighbours = [node2, node3]
node2.neighbours = [node4, node7]
node3.neighbours = [node4, node5]
node4.neighbours = [node6]
node5.neighbours = [node6]
node7.neighbours =  [node6]

g = Graph()
path =g.sssp_bfs(node1, node7)
for i in path:
    print(i.val, end =" ")
 
