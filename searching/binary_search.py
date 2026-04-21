""" Binary Search system to find elements """

import time

def binary_search(array,target):
    arr = sorted(array)
    left = 0
    right = len(array)-1
    target_position = -1
    start = time.perf_counter()

    # main loop
    while left <=right:
        try:
            mid = (left + right) // 2
            if arr[mid] == target:
                target_position = mid
                return  f" Target found at index {mid} time taken: {time_taken:.10f} "
                break
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        except Exception as e:
            return f" Error {e}"
        end = time.perf_counter()
        time_taken = end - start


    if target_position!= -1:
        return f" Target found at index {target_position} and time taken for the algorith : {time_taken:.2f}"
    else:
        return f"Target {target} not found"


# testcases
a1 = [4,7,8,32,234,342,456]
target = 4
print(binary_search(a1,target))

a2 = list(range(1,1000))
target = 745
print(binary_search(a2,target))