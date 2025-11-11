from functools import wraps
from dequeu import deque


def log_method(function):
    """ Main logging function for recording method logs"""
    @wraps(function)
    def wrapper(self,*args,**kwargs):
        #print(f"Method {function} with argument {args} and secondary argumenet {kwargs}")
        result = function(self,*args,**kwargs)
        return result
    return wrapper

class browser():
    """ A browser class with visit back and forward functionality using 2 deques """
    #initiating the main dunders and starters
    def __init__(self,page, page_capacity= None,page_name_limit = None):
        self.page_capacity = page_capacity
        self.page_name_limit = page_name_limit
        self.page = page
        self.front_deque = deque(capacity=page_capacity, page_naming_limit = page_name_limit)
        self.back_deque = deque(capacity=page_capacity,page_naming_limit=page_name_limit)
    def __str__(self):
        return f" Page: {self.page}"
    def is_full(self):
        if len(self.page) == self.page_capacity:
            raise MemoryError("The browser is in it's page holding limit ")
    def is_empty(self):
        if len(self.front_deque) == 0:
            return True
        else:
            return False

    def return_current_page(self):
        return f"Current Page: {self.page}"
    
    #Main functions
    @log_method
    
    def visit(self,url):
        ''' Vist a new site and set it as current '''
        if (not isinstance(url,str)) or  self.is_full() or len(url)>self.page_name_limit:
            return f" Hmmmm can't reach the page Invalid URL "
        else:
            self.front_deque.add_front(url)
            self.current_page = url
            return f"Current Page: {url}"
    
    @log_method
    def back(self):
        ''' Go back to previous page'''
        if not self.is_empty():
            self.back_deque.add_front(self.front_deque.peek_front())
            self.front_deque.remove_front()
            self.current_page = self.front_deque.peek_front()
            return f"Current Page: {self.current_page}"

        else:
            raise IndexError("Cannot go backward you are at the only page {self.page}")

    @log_method
    def forward(self):
        ''' Forward to previous page'''
        if not self.is_empty():
            self.front_deque.add_front(self.back_deque.peek_front())
            self.back_deque.remove_front()
            self.current_page = self.front_deque.peek_front()
            return f"Current Page: {self.current_page}"
        else:
            raise IndexError("Cannot go forward you are at the only page {self.page}")
