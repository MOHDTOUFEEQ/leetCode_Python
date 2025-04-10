class Solution:
    def findMaxAverage(self, nums, k):
        currSum = 0
        
        for i in range(0,k):
            currSum += nums[i]
        
        maxAverage = currSum / k
        
        
        for j in range(k,len(nums)):
            currSum -= nums[j-k]
            currSum += nums[j]
            
            maxAverage = max(maxAverage,currSum / k)
            
        
        return maxAverage