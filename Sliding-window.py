# an array where we need to calcuate maxiumum sum of subarray having size exactly k

# Using brute force algorithm
def max_sum_subarrya(array:list,k:int):
    """ This algorithm is brute force and requires time complexity of O(n*k) and space complexity of 0(1)
    where we n-k+1 is the all numbers of sub arrays we can find """
    n = len(array)
    l = 0
    sums = []
    
    # creatign all sub arrays
    for l in range(n-k+1): # to ensure it does not goes out of bounds
        current_sum = 0
        for i in range(l,l+k):
            current_sum+=array[i]
        sums.append(current_sum)
        l+=1

    return max(sums),elements

a= [5, 2, -1, 0, 3,34,567,34]
# n - k +1   for this case it is 8-3+1 = 6 ie 6 possible combinations

possible_combinaitions = [[5,2,-1],[2,-1,0],[-1,0,3],[0,3,34],[3,34,567]]
print(max_sum_subarrya(a,3))


# Using real sliding technique
def max_sum_subarrya(array: list, k: int):
    """ This algorithm uses the sliding window technique to achieve O(n) time complexity and O(1) space complexity."""
    n = len(array)
    if n < k:
        return f" The size of k is too larger than N"

    # 1. Calculate sum of the first window (first k elements)
    current_sum = sum(array[:k])
    max_sum = current_sum

    # 2. Slide the window from the k-th element to the end
    for i in range(k, n):
        # Update sum: add the new element, subtract the element that left
        current_sum = current_sum + array[i] - array[i - k]

        # Update the max sum if the current window sum is larger
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

x = [23,45,6,774,345,24,56,743,56,56,35]

#Given an array we have to find substring which is repeating and which is not
#Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.


def Max_vowels(arr:int,k:int,n=None)-> int:
    """ Using sliding window technique """
    n = len(arr)
    vowels = ["a","e","i","o","u"]
    max_vowels = 0
    current_vowels = 0

    # creating first cotingent of array
    for i in range(0,k+1):
        if arr[i] in vowels:
            current_vowels += 1

    # creating the second contigent and the sliding window
    for j in range(k,n):
        if arr[j] in vowels:
            current_vowels += 1
            if arr[j-k] in vowels:
                current_vowels -=1

    if current_vowels > max_vowels:
        max_vowels = current_vowels

    return max_vowels
