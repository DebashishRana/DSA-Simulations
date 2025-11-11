import math

# Queue implementation using a list
class queue:
  def __init__(self,capacity):  ## Will intialise the elements and make it work simple'''
     self.items = []
     self.capacity = None

  def __str__(self):
    return str(f" Queue contents rear to front{self.items}")

  def is_empty(self): 
    if len(self.items) == 0:
      return True
    else:
      return False

  def enqueue(self, item): 
      if len(self.items) == self.capacity:
          return 'Queue overflow'
      self.items.insert(0, item)
      return f"{item} enqueued"

  def dequeue(self):
    if not self.is_empty():
        a = self.items.pop()
        return f" Dequed : {a} "
    else:
        return "Queue underflow "

  def len(self):
    x =  len(self.items)
    return f"Length of queue is : {x}"

  def peek_front(self):
    if not self.is_empty():
        return self.items[-1]
    else:
        return "Queue is empty"
  def peek_rear(self):
      if not self.is_empty():
          return self.items[0]
      else:
          return "Queue underflow "

  def front_to_rear(self):
      x = self.items.reverse()
      return f"Queue from front to rear : {x}"

#Code to test the queue class
waiting_list = queue(capacity = math.pow(2,6) )
print(waiting_list.enqueue('David'))
print(waiting_list.enqueue('John'))
print(waiting_list.enqueue('Tina'))
#print(waiting_list.len(), "\n")
#print(waiting_list.dequeue(), "\n")

print(waiting_list, "\n")

print(waiting_list.dequeue(), "\n")
print(waiting_list)
print(waiting_list.front_to_rear)

q2 = queue(capacity=10)

#print(q2.dequeue()) would result in index error as there is nothing to dequeue