### Single Linked List implementation. i.e. Traversal happens only forward
class Node(object):

    def __init__(self,d,n=None,last_node=None): #initialize the Node with data and Null next node
        self.data = d
        self.next_node=n
        self.last_node=last_node

    def get_next(self): ## get the next node object
        return self.next_node

    def set_next(self,n): ## get the next node object
        self.next=n

    def get_data(self): ## get the data of the presebt node object
        return self.data

    def set_data(self,newdata):  ## set the data of a node object
        self.data=newdata

    def get_previous(self):
        pass

class LinkedList(object):
    def __init__(self,r=None): ## inilize the link of the node created . the root/head is none. size of the linked list wit zero
        self.root=r
        self.size=0

    def add(self,newdata): ## add an element at the root/head of the linked list. i.e the new element will the head/root of the linked list
        new_node=Node(newdata,self.root)
        self.root=new_node
        self.size+=1

    def add_tail_c(self,newdata): ## add an element at the end of the linked list. i.e. the new node becomes the next node of last node before adding the new node.
        head=self.root
        while head.next_node: ## get the last node in the list
            head=head.get_next()
        new_node = Node(newdata) ## create a new node
        head.next_node=new_node ## set the new node as the next node of the last node found in previous step
        #head.root=header ## set the root of this new node to the existing root.

    def print_list(self):
        Final=''; head=self.root
        while head:
            if head.next_node:
                Final=Final+str(head.data)+' ,'
            else:
                Final=Final+str(head.data)
            head=head.get_next()
        print((Final))




def main():

    array=[i for i in range (15)]  ### create an array of numbers
    myList= LinkedList() ## create a linked list object

    for elements in array:
        myList.add(elements)  ## add the elements at the begining of the list. See the add function for more details.

    print ("Elements after adding items at the head")
    myList.print_list()

    array=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    for elements in array:
        myList.add_tail_c(elements)  ## add the elements at the begining of the list. See the add function for more details.

    print ("Elements after adding items at the Tail")
    myList.print_list()

    #print(print ("I am here",(print("Hello there"))))
if __name__==main():
    main()