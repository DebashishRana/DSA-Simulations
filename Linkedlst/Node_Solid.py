''' Node class made using Solid principles'''

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

