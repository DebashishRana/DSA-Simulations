# importing stack module 
from stack import stack 
import os 
import timeit 
data1 = ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes', 'Pineapple', 'Strawberry', 'Blueberry', 'Watermelon', 'Papaya']
Stack1 = stack()
Stack1.push(data1)
Stack1.push('Kawasaki')
print(Stack1.peek())
Stack1.pop()
print(Stack1)

print(Stack1.is_empty())

# Question 1 : Rev String using stack
#Write a function rev_string(my_str) that uses a stack to reverse the characters in a string.
def rev_string(my_str):
    s = stack()
    for x in my_str:
        s.push(x)
    rev_str = ""
    while not s.is_empty():
        rev_str+=s.pop()
    return rev_str

print(rev_string("Hello World!")) 

# Question 2 : Check for balanced parentheses using stack
#Write a function is_balanced(my_str) that uses a stack to check if the parentheses in a string are balanced.

def is_balanced(my_str):
    s = stack()
    balanced = True 

    for element in my_str:
            if element =="(":
                s.push(element)
            elif element == ")":
                if s.is_empty():
                    balanced = False
                s.pop()
                   
    if balanced == True and s.is_empty(): 
        return f" {my_str} is balanced"
    else:
        return f"{my_str} is not balanced"

#test_case1 
print(is_balanced("(a + b) * (c + d)"))  

# Question 3  Balanced Symbols
#Write a function is_balanced_symbols(my_str) that uses a stack to check if the symbols in a string are balanced. The symbols to be checked are (), {}, and [].

def is_balanced_symbol(my_str):
    s = stack()
    pairs = {"(": ")", "{": "}", "[": "]"}
    opening = pairs.keys()
    closing = pairs.values()
    for element in my_str:
        if element in opening:
            s.push(element)
        elif element in closing:
            if s.is_empty():
                return f"{my_str} is not balanced"
            top = s.peek()
            if pairs[top] != element:
                return f"{my_str} is not balanced"
            s.pop()
    if s.is_empty():
        return f"{my_str} is balanced"
    else:
        return f"{my_str} is not balanced"
#test cases 1 
case1, case2  = "[ [ { { ( ( ) ) } } ] ]" , " [ ] [ ] [ ] ( ) { }"
print(is_balanced_symbol(case1))
print(is_balanced_symbol(case2))
#test case 2 
case3, case4 = " ( [ ) ]", "( ( ( ) ] ) )"
print(is_balanced_symbol(case3))
print(is_balanced_symbol(case4))
