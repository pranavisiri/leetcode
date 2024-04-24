import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, source, destination, weight):
        if source not in self.vertices:
            self.vertices[source] = []
        if destination not in self.vertices:
            self.vertices[destination] = []
        self.vertices[source].append((destination, weight))
        self.vertices[destination].append((source, weight))

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph.vertices[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
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
shortest_distances = dijkstra(graph, start_vertex)
print("Shortest distances from", start_vertex + ":")
for vertex, distance in shortest_distances.items():
    print("To", vertex + ":", distance)
