#importing modules 
import os 
import timeit

class stack:
    def __init__(self):
        self.items = [] # creates an empty list 
    def push(self,element):
        if element is None:
            raise ValueError('Cannot push None type element in the given stack')
        if element is self:
            raise ValueError('Cannot push stack data type into stack itself')
        self.items.append(element)
        return f"Pushed {element} to stack"
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def __str__(self):
        return f"Stack items: {self.items}"



