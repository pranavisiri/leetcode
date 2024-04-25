'''matrix=[[0 for i in range(5)] for j in range(5)]
matrix[0][0]=1
matrix[2][3]=5
for row in matrix:
    print(row)'''
class Graph:
    def __init__(self,v):
        self.val=v
        self.graph=[[ 0 for i in range(v)] for j in range(v)]
    def add(self,u,v,w):
        self.graph[u][v]=w
        self.graph[v][u]=w
    def print(self):
        for row in self.graph:
            print(" ".join(map(str,row)))
v=int(input())
obj=Graph(v)
obj.add(0,1,3)
obj.add(1,2,5)
obj.add(3,4,6)
obj.add(2,3,10)
obj.add(0,4,7)
obj.add(4,1,11)
obj.add(1,3,2)
obj.print()
