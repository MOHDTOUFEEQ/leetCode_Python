class Solution:
    def productExceptSelf(self, nums):
        suffixSum = []
        prefixSum = [1 for j in nums]
        curr = 1 
        for i in range(0,len(nums)):
            suffixSum.append(curr)
            curr *= nums[i]
            
        curr = 1
        for j in range(len(nums)-1,-1,-1):
            prefixSum[j] = curr
            curr *= nums[j] 
            
            nums[j] = prefixSum[j] * suffixSum[j]
            
        
        return nums