class Graph:
    def __init__(self,v):
        self.v=v
        self.adjlist={i:[]for i in range(v)}
    def add(self,u,v,w):
        self.adjlist[u].append((v,w))
        self.adjlist[v].append((u,w))
    def print(self):
        for i in self.adjlist:
            print(i,"->","->".join(map(str,self.adjlist[i])))
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
