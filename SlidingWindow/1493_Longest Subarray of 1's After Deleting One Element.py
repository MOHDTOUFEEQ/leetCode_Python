class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        
        left = 0 
        right = 0 
        curr = 0
        while right<len(nums):
            if curr > 1:
                while(curr>1):
                    if nums[left] == 0:
                        curr -= 1
                        
                    left += 1
            else:
                if nums[right] == 0:
                    curr += 1
                if curr <2:
                    res = max(res, right - left)
                
                right += 1 
                
        return res