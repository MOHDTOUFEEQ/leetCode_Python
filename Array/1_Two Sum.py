class Solution:
    def twoSum(self, nums, target):
        unique = {}

        for i in range(0,len(nums)):
            diff =  target -  nums[i] 

            if diff in unique:
                return [unique[diff],i]
            else:
                unique[nums[i]] = i


