class Node:
    def __init__(self,val):
        self.value=val
        self.leftChild=None
        self.rightChild=None

    def insert(self,data):
         print ("Self Value {} and Inserting {} ".format(self.value,data))
         if self.value == data:
             return False

         elif self.value > data:
             if self.leftChild:
                 return self.leftChild.insert(data)
             else:
                 self.leftChild=Node(data)
                 return True
         else:
             if self.rightChild:
                 return self.rightChild.insert(data)
             else:
                 self.rightChild = Node(data)
                 return True

    def find(self,data):
        if(self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
              if self.rightChild:
                  return self.rightChild.find(data)
              else:
                  return False

    def preorder(self):
        if self:
            print (str(self.value))
            if self.leftChild:
                print ("Is this left child ",self.leftChild)
                self.leftChild.preorder()
            if self.rightChild:
                print ("Is this right child ",self.rightChild)
                self.rightChild.preorder()

    def postorder(self):
        if self:
            #print ("self is true")
            if self.leftChild:
                #print("left child is true")
                self.leftChild.postorder()
            if self.rightChild:
                #print("right child is true")
                self.rightChild.postorder()
            print (str(self.value))


    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()


class Tree:

    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root:
            print (" Here in insert class : Tree")
            return self.root.insert(data)
        else:
         return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("Preorder")
        self.root.preorder()

    def postorder(self):
        print("postorder")
        self.root.postorder()

    def inorder(self):
        print("inorder")
        self.root.inorder()




bst= Tree()
print (bst.insert(10))
print(bst.insert(12))
bst.insert(1)
bst.insert(400)
bst.insert(500)
bst.insert(3)

#bst.preorder()
#bst.postorder()
#bst.inorder()
