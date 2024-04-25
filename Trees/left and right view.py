class treenode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def left_right_view(root,side):
    if not root:
        return {}
    result={}
    queue=[(root,0)]
    while queue:
        node,level= queue.pop(0)
        if level not in result:
            result[level]=[]
        result[level].append(node.value)
        if node.left:
            queue.append((node.left,level+1))
        if node.right:
            queue.append((node.right,level+1))
    if side=="L":
        print("\n left view")
    else:
        print("\n right view")
    for k in result.keys():
        if(side=='L'):
            print(result[k][0],end=",")
        elif(side=="R"):
            print(result[k][-1],end=",")
root=treenode('A')
root.left=treenode('B')
root.right=treenode('C')
root.left.left=treenode('D')
root.left.right=treenode('E')
root.right.left=treenode('F')
root.right.right=treenode('G')
root.right.right.left=treenode('k')
left_right_view(root,'L')
left_right_view(root,'R')
