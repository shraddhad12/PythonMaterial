class Graph:
    def __init__(self) -> None:
        self.adjecentList = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjecentList.keys():
            self.adjecentList[vertex] = []
            return True
        return False
    
    def add_edges(self, vertex1, vertex2):
        if vertex1 in self.adjecentList.keys() and vertex2 in self.adjecentList.keys():
            if vertex1 not in self.adjecentList[vertex2] and vertex2 not in self.adjecentList[vertex1]:
                self.adjecentList[vertex1].append(vertex2)
                self.adjecentList[vertex2].append(vertex1)
                return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjecentList.keys() and vertex2 in self.adjecentList.keys():
            if vertex1 in self.adjecentList[vertex2] and vertex2 in self.adjecentList[vertex1]:
                self.adjecentList[vertex1].remove(vertex2)
                self.adjecentList[vertex2].remove(vertex1)
        print("No such edge present")

    def remove_vertex(self, vertex):
        if vertex in self.adjecentList.keys():
            del self.adjecentList[vertex]
            for v, e in self.adjecentList.items():
                if vertex in e:
                    self.adjecentList[v].remove(vertex)
            return True
        return False
            
    def print_vertices(self):
        for v, e in self.adjecentList.items():
            print(v, ":", e)

g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edges("A", "B")
g.add_edges("A", "C")
g.add_edges("B", "C")
g.print_vertices()

g.add_edges("B", "A")

g.remove_edge("B", "D")
g.print_vertices()

g.remove_vertex("A")
print("---------")
g.print_vertices()



