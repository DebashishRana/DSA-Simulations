from Node import Node

class Linked_List:
    #initializing constructors
    def __init__(self,Node=None):
        self.head = head
        self.node = Node

    def __str__(self):
        return f"Linked List items {self.head}"

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
    def add(self,item):
        v1 = Node(item)
        v1.set_next_node(self.head)
        self.head = v1

    def size(self):
        current = self.head
        count = 0
        while self.head !=None:
            count+=1
            current = current.next_pointer()
        return count

