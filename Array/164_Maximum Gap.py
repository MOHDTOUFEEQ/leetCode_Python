class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<2:
            return 0
            
        nums.sort()
        
        res = 0
        for i in range(1,len(nums)):
            res = max(nums[i] - nums[i-1],res)
        
        
        
        return res

        