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
    @log_method
    def current_node(self):
        return self.node
    @log_method
    def return_next_node(self):
        return self.next
    @log_method
    def set_next_node(self,new_next):
        if not isinstance(new_next,Node):
            raise ValueError(' Invalid data type a node can only point to another node')
        else:
            self.next=new_next
    @log_method
    def set_data(self,new_data):
        self.node = new_data

    if __name__ == "__main__":
        Node()

# Test Cases

Node1 = Node(10)
Node2= Node(20)
Node1.set_next_node(Node2)

print((Node1))
print((Node1.return_next_node()))
print(type(Node1))


class Node_SOLID:
    def __init__(self,current_pointer,next_pointer=None):
        self.current_pointer= current_pointer
        self.next_pointer = next_pointer
    def __str__(self):
        return f" Node: {self.current}"

    @property
    def current_pointer(self):
        return self.current

    @current_pointer.setter
    def new_current_pointer(self,new_node):
        self.current_pointer = new_node

    @property
    def next_pointer(self):
        return self.next_pointer
    @next_pointer.setter
    def new_next_pointer(self,new_pointer):
        if not isinstance(new_pointer,Node):
            raise ValueError(" Forward pointer can only be a Node class")
        else:
            self.next_pointer = new_pointer







