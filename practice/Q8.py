#implememntation of a car wash
'''' We would be using Deque ADT'''

from collections import deque

class car_wash():
    def __init__(self,capacity=None):
        self.items = deque()
        self.capacity = capacity
    
    def enter_carwash(self,car):
        self.items.eneque(car)
        self.capacity -=1
        return "You've entered the car wash"
        
    
    def exit_carwash(self):
        if self.items() == 0:
            return f" Hey no ones there in the car wash so whos' going out"
        self.items.deque()
        self.capacity +=1
    
    def current_car(self):
        return self.items[]
    
    
