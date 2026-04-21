""" Binary Search system to find elements """

def binary_search(array,target):
    arr = sorted(array)
    left = 0
    right = len(array)-1
    mid = (left+right)//2

    while left <=right:
        if arr[mid] == target:
            return  f" Target found at index {mid}"
        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid -1

    result = -1

    if result!= -1:
        return f" Target found at index {result}"
    else:
        return "Target not found"


# testcases
a1 = [1,2,3,4,5]
target = 4
print(binary_search(a1,target))