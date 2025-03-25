class Solution:
    def maxSubarraySumCircular(self, nums):
        res = sum(nums)
        
        Currmin = nums[0]
        Maxmin = nums[0]
        
        Currmax = nums[0]
        Maxmax = nums[0]
        
        for i in range(1,len(nums)):
            if Currmax + nums[i] > nums[i]:
                Currmax = Currmax + nums[i]
            elif Currmax + nums[i] <= nums[i]:
                Currmax = nums[i]
                
            if Currmin + nums[i] < nums[i]:
                Currmin = Currmin + nums[i]
            elif Currmin + nums[i] >= nums[i]:
                Currmin = nums[i]
            
            Maxmin = min(Maxmin,Currmin)
            Maxmax = max(Maxmax,Currmax)
            res = max(res,nums[i])

        if sum(nums) == Maxmin:
            return Maxmax 
        res = max(Maxmax,(sum(nums)-Maxmin))
        return res