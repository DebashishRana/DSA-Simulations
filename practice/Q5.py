    #implementing the Queue ADT using a list such that rear of the the queue is at the end of the list 
#[1,2,3,4,5] example here so the first item needs to be the 1st item and the 5th element need be the last 
        
class Soultion:
    def __init__(self):
        self.items =  []
    
    def eneque(self,item):
        self.items.append(item)
    
    def is_empty(self):
        
        if len(self.items) == 0:
            return True
        else:
            return False

    def deque(self):
        if self.is_empty:
            raise IndexError("No items to pop")
        self.items.pop(0)
    
    def __str__(self):
        return f"Items: {self.items}"

x = Soultion()
x.eneque(1)
x.eneque(2)
x.eneque(4)
x.eneque(5)

print(x)