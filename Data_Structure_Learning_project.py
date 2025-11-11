#importing modules 
from random import randrange
from xml.dom import IndexSizeErr
from random import randint
from random import random
import timeit
from timeit import Timer
from stack import stack

''' This algorithm uses standard list '''
def min_finder_standard(array):
    #integrity check 
    if not isinstance(array,list):
        print( ConnectionError(f" Invalid data type this function takes only lists "))
        print('Converting to lists .......')
        array = list(array)
    else: 
        
        stack = list(array) # we can itrate and check in less for larger 
        #doble iteration 
        for x in range(len(stack)):
            for y in range(len(stack)):
                x_is_min = True
                if stack[x] > stack[y]:
                    x_is_min = False
                    break
            return stack[x] if x_is_min else stack[y] #worst case scenario

''' This algorith tries to optimze the time complexity by using sets to reduce o(N) '''
def min_finder_setter(array):
    #integrity check 
    if not isinstance(array,list):
        print( ConnectionError(f" Invalid data type this function takes only lists "))
        print('Converting to lists .......')
        array = list(array)
    else: 
        setted = set(array)
        stack = list(setted) # we can itrate and check in less for larger 
        #doble iteration 
        for x in range(len(stack)):
            for y in range(len(stack)):
                x_is_min = True
                if stack[x] > stack[y]:
                    x_is_min = False
                    break
            return stack[x] if x_is_min else stack[y] #worst case scenario

'''Using O(n)'''
def min_finder2(array):
    #integrity check on array 
    if not isinstance(array,list):
        print("Input wasn't a list \n Converting ...... ")
    orginal_stack = list(array)
    new_stack = []
    for x in range(len(orginal_stack)):
        new_stack.append(orginal_stack[x])
    return min(new_stack)
    
#alter code using 0(log(n))

def min_finder3(array):
    if not isinstance(array,list):
        print("Input wasn't a list \n Converting ...... ")

    # applying bubble soritng algortihm 
    orginal_stack = list(array)
    new_stack = sorted(orginal_stack) 
    return new_stack[0] if new_stack else None

test_array = [1,2,36,77]
#print(min_finder2(test_array))

test_array2 = [100,1003,345,677,9844]
#print(min_finder_standard(test_array))
print("\n")
#print(min_finder_optimized(test_array2))
#print(min_finder3(test_array))

'''Case 1'''
''' In this experemint the reults being''' 
data  = randint(1,1000000)
#Standard algorithm timing finding min val for 1 million records 0.009529599999950733 seconds
#Optimized algorithm timing finding min val for 1 million records 0.2577854000001025 seconds

#the reson must be due to low redudancy or none for the data due to which set funtion took another O(n) and thus it got late by few miliseconds
data  = randint(1,1000000) # as the data was not redundant rahter unique 
test_data1 = [randint(1,1000000) for x in range(1000000)]
test_data2 = [randint(1,1000000) for y in range(1000000)]
t1 = Timer(stmt = "min_finder_standard(test_data1)",
          setup= "from __main__ import min_finder_standard,test_data1")
print(f'Stack algorithm timing finding min val for 1 million records was {t1.timeit(number=1)} seconds' )

t2 = t1 = Timer(stmt = "min_finder_setter(test_data2)",
          setup= "from __main__ import min_finder_setter,test_data2")
print(f'Stack set algorithm timing finding min val for 1 million records was  {t2.timeit(number=1)} seconds \n \n')

'''Case 2'''
''' Here the data being redundat'''
data1 = test_data1*4
# and 
data2 = test_data2*4
# appending thrice

# appending data 3 twice
t3 = Timer(stmt = "min_finder_standard(data1)",
          setup= "from __main__ import min_finder_standard,data1")
print(f'Stack architecture algorithm timing finding min val for 1 million records which was redundant quadratic times was {t3.timeit(number=1)} seconds' )

t4 =  Timer(stmt = "min_finder_setter(data2)",
          setup= "from __main__ import min_finder_setter,data2")
print(f'Stack set timing finding min val for 1 million records redundat quadratic time was  {t4.timeit(number=1)} seconds')

'''Output '''
#Stack architecture algorithm timing finding min val for 1 million records which was redundant quadratic times was 0.07531200000084937 seconds
#Stack set timing finding min val for 1 million records redundat quadratic time was  0.9819661000001361 seconds


 # hence we can argue using sets actually adds burden to the algorth due to the O(n) function behaviour of the set function




""" An experiment to check the time efficiency of Hashmaps over stacks """







# importing modules 
from timeit import Timer
from random import randint

# Question 1 
''' Experiment to prove list index function is O(1) notation '''
# ie we have to prove that no matter the index we are accessing in a list the time taken to return it is constant

# def return_first_index(stack):
#   return stack[0]

# def return_middle_index(stack):
#   mid_pos = len(stack)//2
#   return stack[mid_pos]

# def return_last_index(stack):
#   return stack[-1]

# data = [randint(1,1000000) for x in range(1000000)]

# # experiments for proving the time complexity of list index function is o(1) ie constant 

# func1_time = timer(stmt="return_first_index(data)",
#                   setup="from __main__ import return_first_index, data")
# func2_time = timer(stmt="return_middle_index(data)",
#                   setup="from __main__ import return_middle_index, data")
# func3_time = timer(stmt="return_last_index(data)",
#                   setup="from __main__ import return_last_index, data")

t1 = round((func1_time.timeit(number=1)),4)
print(f'time taken to access the first index in the list is {t1} seconds \n')
t2 = round((func2_time.timeit(number=1)),4)
print(f'time taken to access the middle index in the list is {t1} seconds \n')
t3 = round((func3_time.timeit(number=1)),4)
print(f'time taken to access the last index in the list is {t1} seconds \n')

# if t1==t2==t3:
#   print(f"hence proven \ntime taken to access the first middle and the last index element in a list is constant as the difference is {round(t1,4)} seocnds")
# else:
#   print(f"time taken to access the first middle and the last index element in a list is not constant the difference is {round(t1-t2,4)} seoncds and {round(t2-t3,4)}seconds")



''' Question 2 
    Devise an experiment to verify that get item and set item are O(1) for dictionaries. '''
# Setting up 

def Question2(data):
  data1 = [x for x in range(1000000)]
  data2 = [y for y in range(1000000000)]
  data3 = [z for z in range(1000000000000)]
  
  first_index_data1= data1[0]
  first_index_data2= data2[0]
  first_index_data3= data3[0]
  
  mid_index_data1 = data[len(data1)//2]
  mid_index_data2 = data[len(data2)//2]
  mid_index_data3 = data[len(data3)//2]
  
  last_index_data1 = data1[-1]
  last_index_data2 = data2[-1]
  last_index_data3 = data3[-1]
  
  # Creatign a stack 
  dict1 = {}
  for y in enumerate(data1):
    dict1[y] = y
  
  dict2 = {}
  for y in enumerate(data2):
     dict2[y] = y
  
  dict3 = {}
  for y in enumerate(data1):
    dict3[y] = y

    
  return dict1, dict2,dict3
  
  



