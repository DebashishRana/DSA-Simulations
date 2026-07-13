 
def findMaxAverage(nums: list[int], k: int) -> float:
        
        left = 0 
        n = len(nums)
        averages = []
        
        
        while left<n-1:
            sum = 0 
            for x in range(left,left+k):
                sum += nums[x]
                avg = sum/k
                averages.append(avg)
            left+=1 
            
        max_avg = max(averages)
        return max_avg
        
example = [1,12,-5,-6,50,3]
k = 3
print(findMaxAverage(example,k))