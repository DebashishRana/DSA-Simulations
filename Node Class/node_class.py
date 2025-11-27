# Initializing Main dunder
from functools import  wraps

def log_method(func):
    @wraps(func)
    def wrapper (self,*args,**kwargs):
        result = func(self,*args,**kwargs)
        return result
    return wrapper

class Node:
    ''' Node class basic code with implementation of Node current setting and returning '''
    def __init__(self,node_val,next_val=None):
        self.node = node_val
        self.next = next_val

    def __str__(self) -> str :
        return f"Node: {self.node}"
    #Main log methods
    @log_method
    def current_node(self):
        return self.node

    @log_method
    def next_pointer(self):
     return self.next

    @log_method
    def set_next_pointer(self,new_next):
        if not isinstance(new_next,Node):
            raise ValueError(' Invalid data type a node can only point to another node')
        else:
            self.next=new_next
    @log_method
    def set_data(self,new_data):
        ''' Creates the new data as the main data'''
        self.node = new_data

    if __name__ == "__main__":
        Node()

# Test Cases




























