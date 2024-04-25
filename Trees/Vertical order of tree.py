class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def vertical_order(root):
    vertical_map={}
    q=[(root,0)]
    while q:
        Node,hd=q.pop(0)
        if hd not in vertical_map:
            vertical_map[hd]=[]
        vertical_map[hd].append(Node.data)
        if Node.left:
            q.append((Node.left,hd-1))
        if Node.right:
            q.append((Node.right,hd+1))
    print("vertical order traversal")
    for hd in sorted(vertical_map):
        print(vertical_map[hd],end=",")

root=Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left=Node('D')
root.left.right=Node('E')
root.right.left=Node('F')
root.right.right=Node('G')
vertical_order(root)
