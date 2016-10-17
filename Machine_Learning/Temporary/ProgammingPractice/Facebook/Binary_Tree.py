class Node():
    def __init__(self,val):
        self.value=val
        self.root=None
        self.leftchild=None
        self.rightchild=None



def insert_node(root,node):
    if root is None:
        root=Node

    else:
        if root.value> node.value:
            if root.leftchild is None:
                root.leftchild=node
            else:
                insert_node(root.leftchild,node)
        else:
            if root.value<= node.value:
                if root.rightchild is None:
                    root.rightchild=node
                else:
                    insert_node(root.rightchild,node)



def pre_order(root):

 if root is not None:
     print(root.value)
     pre_order(root.leftchild)
     pre_order(root.rightchild)


#def inorder():

#def post_order():



r = Node(3)
insert_node(r, Node(7))
insert_node(r, Node(100))
insert_node(r, Node(5))
insert_node(r, Node(-1))

pre_order(r)