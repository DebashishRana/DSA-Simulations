#importin functions 
from functools import wraps 

def log_method(func): # this logging decorator takes another function as an argument
    @wraps (func) # this function wraps the function but brands to preserve it's metadata like name and docstring
    def wrapper(self,*args, **kwargs): #args and kwargs to handle any number of arguments where ar is no. of unnamed arguments whereas for kwars it's named pair items like dictionary
        # print(f"Method called {func.__name__} where args: {args} and  kwargs: {kwargs}")
        result = func(self, *args, **kwargs)
        # print(f"Method {func.__name__} returned {result}")
        return result
    return wrapper

class deque:
    #definin key functions
    def __init__(self,capacity=None, page_naming_limit = None):
        self.items = []
        self.capacity =capacity
        self.name_limit = page_naming_limit
    def __str__(self):
        """ Return string representation of the deque """
        return f"Deque items : {self.items}"
    
    def is_full(self):
        if len(self.items)==self.capacity:
            return f"Unable to add more items , Deque overflow expected in more input "
    def is_empty(self):
        if len(self.items)==0:
            return f"Deque is empty , underflow expected in more removal"
    def size(self):
        return len(self.items)
    
    # key methods with logging decorator
    @log_method
    def add_front(self,item):
        if self.is_full() or self.name_limit is not None and item > self.name_limit:
            return IndexError (self.is_full())
        else:
            self.items.append(item)
    @log_method 
    def add_rear(self,item):
        if self.is_full():
            return IndexError(self.is_full())
        else:
            self.items.insert(0,item)
    @log_method 
    def remove_front(self):
        if not self.is_empty():
            self.items.pop()
        else:
            return IndexError(f"Deque Underflow expected , Deque is empty")
    @log_method 
    def remove_rear(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            return IndexError(f"Deque Underflow expected , Deque is empty")
    @log_method 
    def peek_front(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return IndexError(f"Deque is empty , no front item available")
    @log_method 
    def peek_rear(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return IndexError(f"Deque is empty , no rear item available")\

if __name__ == "__main__":
    deque()