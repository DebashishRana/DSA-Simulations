# Recursions using Python

# Normal function for addition
def list_sum(num_list):
    sum = 0
    for x in num_list:
        sum+=x
    return sum

# Recursive function for addition
def list_sum_rec(num_list):
    #base case
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum_rec(num_list[1:])

print(list_sum_rec([1,3,5,7,9]))

#Factorial
def factorial_recursion(n):

    if n == 0:
        raise IndexErrorrror("Factorial of Zero is Zero!")
    if n ==1:
        return 1
    else:
        factorial = n * factorial_recursion(n-1)
        return factorial

print(factorial_recursion(4))


def to_str(n,base):
    convert_string  = "0123456789ABCDEF"
    if n<base:
        return convert_string[n]
    else:
        return to_str(n// base,base) + convert_string[n%base]

print(to_str(1453,16))





