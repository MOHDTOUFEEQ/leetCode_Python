class Solution:
    def longestOnes(self, nums, k: int) -> int:
        res = 0
        
        left = 0 
        right = 0 
        curr = 0
        while right<len(nums):
            if curr > k:
                while(curr>k):
                    if nums[left] == 0:
                        curr -= 1
                        
                    left += 1
            else:
                if nums[right] == 0:
                    curr += 1
                    
                if curr<=k:
                    res = max(res, right - left + 1)
                
                right += 1 
                
        
        return res