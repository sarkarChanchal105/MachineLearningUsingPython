### Double Linked List implementation. i.e. Traversal happens forward and backward direction
class Node(object):

    def __init__(self,d,n=None,p=None): #initialize the Node with data and Null next node
        self.data = d
        self.next_node=n
        self.previous_node=p
        print ("Initilizing with data :{} next_node :{} previous_node: {} ".format(self.data,self.next_node,self.previous_node))

    def get_next(self): ## get the next node object
        return self.next_node

    def set_next(self,n): ## get the next node object
        self.next=n

    def get_data(self): ## get the data of the presebt node object
        return self.data

    def set_data(self,newdata):  ## set the data of a node object
        self.data=newdata

    def set_previous(self,p):
        self.previous_node=p

    def get_previous(self):
        return self.previous_node

class LinkedList(object):
    def __init__(self,r=None,p=None): ## inilize the link of the node created . the root/head is none. size of the linked list wit zero
        self.root=r
        self.previous_node=p
        self.size=0

    def add(self,newdata): ## add an element at the root/head of the linked list. i.e the new element will the head/root of the linked list
        if self.root:
            print ("self.Root : {} Data : {}".format(self.root,self.root.get_data()))
        else:
            print ("self.Root : {} ".format(self.root))
        new_node = Node(newdata,self.root)
        if self.root:
            self.root.set_previous(new_node)
        self.root=new_node
        self.size=+1

    def add_tail_c(self,newdata): ## add an element at the end of the linked list. i.e. the new node becomes the next node of last node before adding the new node.
        head=self.root
        while head.next_node: ## get the last node in the list
            head=head.get_next()
        new_node = Node(newdata) ## create a new node
        head.next_node=new_node ## set the new node as the next node of the last node found in previous step
        #head.root=header ## set the root of this new node to the existing root.

    def remove(self,data):
        this_node=self.root
        while this_node:
            if this_node.get_data()==data:
                next=this_node.get_next()
                previous=this_node.get_previous()
                if next:
                    next.set_previous(previous)
                if previous:
                    previous.se_next(next)
            else:
                this_node.get_next()


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

    myList= LinkedList() ## create a linked list object
    myList.add(5)
    myList.add(6)
    myList.add(7)
    myList.add_tail_c(8)
    myList.print_list()


    head=myList.root

    # print (head.data)
    # print (head.next_node.data)
    # print (head.next_node.previous_node.data)

    # array=[i for i in range (15)]  ### create an array of numbers
    # for elements in array:
    #     myList.add(elements)  ## add the elements at the begining of the list. See the add function for more details.
    #
    # print ("Elements after adding items at the head")
    # myList.print_list()
    #
    # array=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    # for elements in array:
    #     myList.add_tail_c(elements)  ## add the elements at the begining of the list. See the add function for more details.
    #
    # print ("Elements after adding items at the Tail")
    # myList.print_list()

if __name__==main():
    main()