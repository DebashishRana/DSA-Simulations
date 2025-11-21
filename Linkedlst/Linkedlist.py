from node_class import Node
from functools import  wraps

def log_method(func):
    @wraps(func)
    def wrapper(self,*args,**kwargs):
        result = func(self,*args,**kwargs)
        return f" Wrapper result {result}"
    return wrapper

class Linked_List:
    #initializing constructors
    def __init__(self,next=None):
        if not isinstance(next,Node):
            self.next = Node(next)
        self.head = Node(head)

    def __str__(self) ->str:
        return f"Linked List items {self.head}"

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    @log_method
    def add(self,item):
        v1 = Node(item)
        v1.set_next_node(self.head)
        self.head = v1

    @log_method
    def size(self):
        current = self.head
        count = 0
        if self.head == None:
            return f" The Linked List is empty "
        else:
            while self.head !=None:
                count+=1
                current = current.next_pointer()
        return count

    @log_method
    def search(self,item):

        current = self.head #self.head is a node class
        found = False
        index = 0
        #main iteration
        while current!=None :
            if current.node == item:
                found = True
                break
            else:
                current = current.next_pointer
                index+=1

        if found:
            return f" Item {item} indexed at {index} is present in the structure "
        else:
            return f"The item {item} is not present in the Linkedlist"

    @log_method
    def remove(self,item):
        current = self.head
        previous = None
        found = False

        while not Found:
            if current == item:
                found = True
            else:
                previous = current
                current = current.next_pointer()
        if previous == None: #when the head is the item itelsef we just unlink the head and make the next pointer the head
            self.head == current.next_pointer()
        else:
            previous.set_next_pointer(current.next_pointer) # the previous item of current  items would point to the item next of current item which would make previous connect with currents next pointer

    @log_method
    def append(self,item):
        ''' Adds an item at the end of the nodes pointers such that next to that item is None'''
        pass