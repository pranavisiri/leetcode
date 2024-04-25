class Graph:
    def __init__(self, v, e):
        self.v = v
        self.e = e
        self.incidence_matrix = [[0] * e for _ in range(v)]

    def add_edge(self, edge, u, v):
        self.incidence_matrix[u][edge] = 1
        self.incidence_matrix[v][edge] = -1

    def print_incidence_matrix(self):
        for row in self.incidence_matrix:
            print(row)


# Taking input for the number of vertices and edges
v = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))

# Creating a Graph object with v vertices and e edges
obj = Graph(v, e)

# Adding edges
obj.add_edge(0, 0, 1)
obj.add_edge(1, 1, 2)
obj.add_edge(2, 3, 4)
obj.add_edge(3, 2, 3)
obj.add_edge(4, 0, 4)
obj.add_edge(5, 4, 1)
obj.add_edge(6, 1, 3)

# Printing the incidence matrix representation of the graph
print("Incidence Matrix:")
obj.print_incidence_matrix()
