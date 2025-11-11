# imporitng modules 
from stack import stack

def decimal_to_binary(n):
    bin_stack = stack()
    decimal = n
    binary_stack = ""

    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal//2
        bin_stack.push(remainder)
    
    #reversing a stack
    while not bin_stack.is_empty():
        binary_stack+=str(bin_stack.pop())
    return f"0b {binary_stack}" 


a =10 
print(decimal_to_binary(a))