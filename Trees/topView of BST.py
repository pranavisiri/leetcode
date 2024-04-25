class Node:
    # Construct to create a newNode
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None
        self.hd = 0
def constructtree(nodelist):
    root=Node(nodelist[0])
    root.left=Node(nodelist[1])
    root.right=Node(nodelist[2])
    root.left.left=Node(nodelist[3])
    root.left.right=Node(nodelist[4])
    root.right.left=Node(nodelist[5])
    root.right.right=Node(nodelist[6])
    return root
def topview(root):
    m={}
    q=[]
    q=[root]
    while len(q)>0:
        cur_node=q.pop(0)
        if cur_node.hd not in m:
            m[cur_node.hd]=cur_node.data
        if cur_node.left:
            cur_node.left.hd=cur_node.hd-1
            q.append(cur_node.left)
        if cur_node.right:
            cur_node.right.hd=cur_node.hd+1
            q.append(cur_node.right)
    #m=sorted(m)
    print("top view")
    for key in sorted(m):
        print(m[key],end=",")
    #for k,v in m.items():
        #print(v,end=",")
nodelist=['A','B','C','D','E','F','G']
root=constructtree(nodelist)
topview(root)
            
