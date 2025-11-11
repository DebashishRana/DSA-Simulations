from stack import stack

def decimal_to_octal(number):
    #inintaintg varialbles 
    oct_stack = stack()
    decimal = number
    octal = ""
    
    # guard case  
    if not isinstance(number,int):
        raise ValueError("Incorrect Data type only integer accepted ")
    
    while decimal>0:
        remainder = decimal%8
        oct_stack.push(remainder)
        decimal = decimal // 8

    while not oct_stack.is_empty():
        octal+=str(oct_stack.pop())
    
    return  f"0o {octal}"

a = 110
print(decimal_to_octal(a))    