#importing modules

from functools import wraps

def log_method(func):
    @wraps(func)
    def wrapper(self,*args,**kwargs):
        result = func(self,*args,**kwargs)
        retrun f"Function Result: {result}"
    return wrapper

class Node:
    #initializing the dunder
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"Node items : {self.data}"
    #setting properties and methods
    @log_method
    @property
    def data(self):
        ''' Getter method for data extraction'''
        return self.data

    @log_method
    @property
    def next(self):
        return self.next

    @log_method
    @data.setter
    def data(self,data):
        if isinstance(data,None):
            raise ValueError(f" Invalid Data Strucutre None cannot be an element")
        if not isinstance(data,Node):
            data = Node(data)
            except Exception as e:
            return f"Error {e}"
        else:
            self.data = data
    @log_method
    @next.setter
    def next(self,next):
        if isinstance(next,None):
            raise ValueError(f" Invalid Data type {None} cannot be a an element of linked list")
        if not isinstance(next,Node):
            next = Node(next)
            except Exception as e:
            return f" Error :  {e}"








