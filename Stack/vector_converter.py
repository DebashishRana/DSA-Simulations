#importing modules 
from multiprocessing.resource_tracker import ResourceTracker
from sqlite3 import Binary
from typing import Type

def decimal_to_binary(num):
    deci = str(int(num))
    holder = []
    post_decima = []
    for x in deci.split("."):
        holder.append(x)
    # main conversion 
    #post_decima.append(holder.pop)
    main_value = holder[0] # still a str 
    reverse  = "".join(reversed(main_value))
    #return reverse
    result = 0 
    for index , value in enumerate(reverse,start=0):
        digit = int(value)
        result += num*(2**index)

    return result
    
    
d1 = 113.0
print(decimal_to_binary(d1))
        

