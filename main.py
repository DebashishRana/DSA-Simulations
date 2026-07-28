def two_pointers_sum_fast_and_slow(nums:list,target:int) ->int:
    """ Main implementation of Two pointers fast and slow algorithm works on sorted array only with Time Complexity O(n) and Space
    complexity of O(1) respectively """

    if not isinstance(nums,list):
        raise ValueError("nums must be a list")
    n = len(nums)
    main = sorted(nums)
    left = 0
    right = n-1
    while left<right:
        current_sum = main[left] + main[right]
        if current_sum == target:
            return main[left],main[right]
        elif current_sum < target:
            left+=1
        else:
            right -= 1
    return None

l1 = [1,2,3,4,5,6]
target  = 9
print(two_pointers_sum_fast_and_slow(nums=l1,target=target))