class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_edge(self, source, destination, weight):
        self.vertices.setdefault(source, []).append((destination, weight))
        self.edges.append((source, destination, weight))
        # Make sure destination vertices are included in the vertices dictionary
        if destination not in self.vertices:
            self.vertices[destination] = []

def bellman_ford(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start] = 0

    # Relax all edges |V| - 1 times
    for _ in range(len(graph.vertices) - 1):
        for source, destination, weight in graph.edges:
            if distances[source] + weight < distances[destination]:
                distances[destination] = distances[source] + weight

    # Check for negative cycles
    for source, destination, weight in graph.edges:
        if distances[source] + weight < distances[destination]:
            print("Graph contains negative cycle!")
            return

    return distances

# Example usage:
graph = Graph()
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 5)
graph.add_edge('B', 'D', 10)
graph.add_edge('C', 'D', 3)
graph.add_edge('C', 'E', 7)
graph.add_edge('D', 'E', 8)

start_vertex = 'A'
shortest_distances = bellman_ford(graph, start_vertex)
if shortest_distances:
    print("Shortest distances from", start_vertex + ":")
    for vertex, distance in shortest_distances.items():
        print("To", vertex + ":", distance)
