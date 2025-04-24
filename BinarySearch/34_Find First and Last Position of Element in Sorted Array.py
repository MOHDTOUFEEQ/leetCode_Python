import math
class Solution:
    def searchRange(self, nums, target):
        def backtracking(left1):
            left = 0
            right = len(nums) - 1
            res = -1
            while(left <= right):
                mid = math.floor((left+right)/2)
        
                if nums[mid] == target:
                    res = mid
                    if left1 is True:
                        right = mid - 1
                    else:
                        left = mid + 1
                        
                elif nums[mid]<target:
                    left = mid + 1
        
                else:
                    right = mid - 1
            return res
        
        return [backtracking(True),backtracking(False)]