import heapq

class PrimMST:
    def __init__(self):
        self.vertices = {}
        self.visited = set()

    def add_edge(self, v1, v2, weight):
        if v1 not in self.vertices:
            self.vertices[v1] = []
        if v2 not in self.vertices:
            self.vertices[v2] = []
        self.vertices[v1].append((v2, weight))
        self.vertices[v2].append((v1, weight))

    def prim(self, start_vertex):
        minimum_spanning_tree = []
        heap = []
        total_cost = 0
        self.visited.add(start_vertex)
        self.populate_heap(heap, start_vertex)

        while heap:
            weight, vertex, neighbor = heapq.heappop(heap)
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                minimum_spanning_tree.append((vertex, neighbor, weight))
                total_cost += weight
                self.populate_heap(heap, neighbor)

        return minimum_spanning_tree, total_cost

    def populate_heap(self, heap, vertex):
        for neighbor, weight in self.vertices[vertex]:
            if neighbor not in self.visited:
                heapq.heappush(heap, (weight, vertex, neighbor))

# Example usage:
graph = PrimMST()
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 5)
graph.add_edge('B', 'D', 10)
graph.add_edge('C', 'D', 3)
graph.add_edge('C', 'E', 7)
graph.add_edge('D', 'E', 8)

minimum_spanning_tree, total_cost = graph.prim('A')

print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
print("Total Cost:", total_cost)
