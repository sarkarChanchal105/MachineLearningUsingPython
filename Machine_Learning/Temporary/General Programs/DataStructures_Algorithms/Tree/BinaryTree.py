class node():
    def __init__(self,val):
        self.l_child=None
        self.r_child=None
        self.data=val

def  binary_insert(root,node):
        if root is None:
            root=node
        else:
            if root.data > node.data:
                if root.l_child is None:
                    root.l_child=node
                else:
                    binary_insert(root.l_child,node)
            else:
                if root.r_child is None:
                    root.r_child=node
                else:
                    binary_insert(root.r_child,node)


def inorder(root):

    if not root:
        return
    print(root.data)
    inorder(root.l_child)
    print(root.data)
    inorder(root.r_child)

def pre_order(root):

    if not root:
        return
    print (root.data)
    pre_order(root.l_child)
    pre_order(root.r_child)

def postorder(root):

    if not root:
        return
    postorder(root.l_child)
    postorder(root.r_child)
    print(root.data)

r = node(3)
binary_insert(r, node(7))
binary_insert(r, node(100))
binary_insert(r, node(5))
binary_insert(r, node(-1))

print ("Runnig In Order")
inorder(r)
print ("Runnig Pre Order")
pre_order(r)
print ("Runnig Post Order")
postorder(r)