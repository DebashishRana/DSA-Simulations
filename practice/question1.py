# Using stack of remainders to calculate binary using divide by 2
from pickle import FALSE

from Stack_class import  stack

def decimal_to_binary(decimal):
    if not isinstance(decimal,int):
        raise  ValueError(f" The application accepts integers only for now")
    rem_stack = stack()
    binary = ""

    while decimal>0:
        remainder = int(decimal%2)
        rem_stack.push(remainder)
        decimal = int(decimal / 2)
    while not rem_stack.is_empty():
        binary+=str((rem_stack.pop()))

    return binary

''' Test Cases '''
Edge_test_1 = "Hello World "
Value_test_2 = 17
#print(f" Test : {decimal_to_binary(test_1)} \n") # Edge cases detection is working
print(f" Test 1: \n 0o: {decimal_to_binary(Value_test_2)}")

Test_Value_3 = 45
print(f"Test 2 \n 0o {decimal_to_binary(Test_Value_3)} ")

Test_Value_4 = 96
print(f"Test 3 \n 0o {decimal_to_binary(Test_Value_3)} ")
# Iterative test cases
if bin(45)[2:] == decimal_to_binary(Test_Value_3) or bin(96)[2:] == decimal_to_binary(45) or bin(17)[2:] == decimal_to_binary(17) :
    print(f" {True} the values equate adequately the algorthm wokrs" )
else:
    print(f"{FALSE} the values dont equate adequately ")