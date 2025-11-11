from functools import wraps

def log_method(function): #main logging function 
    @wraps (function) #creating a wrap 
    def wrapper(self, *args, **kwargs): #what the wrapper does 
        print( f"Method called {function.__name__} with args: {args} and secondary argument {kwargs}")
        result = function(self,args,kwargs)
        print(f"Method {function.__name__} returned {result}")
        return result
    return wrapper

class deque():
    # Initializing main dunders 
    def __init__(self,capacity= None, max_val= None):
        self.capacity = capacity
        self.max_val = max_val
        self.items = []
    
    def __str__(self):
        return self.items
    
    def is_empty(self):
        if len(self.items == 0):
            return True
        else:
             return False 
    def is_full(self):
        if len(self.items) == self.capacity:
            return True 
        else:
            return False
    
    ''' Main Functions '''
@log_method 
def add_front(self,item):
    if self.is_full() or item>self.max_val :
        return IndexError("Unable to add items Deque overflow ")
    else:
        self.items.append(item)
@log_method 
def add_rear(self,item):
    if self.is_full() or item>self.max_val :
        return IndexError("Unable to add items Deque overflow ")
    else:
        self.items.insert(0,item)
@log_method
def  remove_front(self):
    if self.is_empty():
        return IndexError('Deque underflow unable to remove item')
    else:
        self.items.pop(0)

@log_method 
def peek_front(self):
    if not self.is_empty():
        return self.items[-1]
    else:
        return IndexError("Deque underflow no items in data strucutre to peek")

@log_method
def peek_rear(self):
    if not self.is_empty():
        return self.items[0]
    else:
        return IndexError("Deque underflow no items in data strucutre to peek")