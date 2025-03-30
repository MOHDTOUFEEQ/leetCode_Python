import math
class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums)-1
        
        while(left<right):
            mid = math.floor((left+right)/2)
            
            if(nums[mid]>nums[mid+1]):
                right = mid
            else:
                left = mid + 1
            
        
        return left