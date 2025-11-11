from stack import stack

def decimal_to_hex(number):
    
    #inintating variables 
    hex_stack = stack()
    decimal = number
    values = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    hexadecimal = ""

    if  not isinstance(number, int):
        raise ValueError("Incorrect Data type only integer accepted ")
    if decimal == 0:
        return "0x 0"
    else:
        while decimal > 0:
            remainder = decimal%16
            hex_stack.push(remainder)
            decimal = decimal //16

    while not hex_stack.is_empty():
        hexadecimal += str(values[hex_stack.pop()])

    return "0x " + hexadecimal


a = 1999 
print(decimal_to_hex(a))