# an array where we need to calcuate maxiumum sum of subarray having size exactly k

# Using brute force algorithm
def max_sum_subarrya(array:list,k:int):
    n = len(array)
    l = 0
    sums = []
    elements = []
    # creatign all sub arrays
    for l in range(n-k+1): # to ensure it does not goes out of bounds
        current_sum = 0
        for i in range(l,l+k):
            current_sum+=array[i]

        elements.append(i)
        sums.append(current_sum)
        l+=1
    return max(sums),elements

a= [5, 2, -1, 0, 3]
print(max_sum_subarrya(a,3))
