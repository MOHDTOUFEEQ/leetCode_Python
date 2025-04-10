class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float("-inf")
        
        for i in range(0,len(nums)-2):
            j = i + 1
            k = len(nums) -1 
            while(j<k):
                total = nums[i] + nums[j] + nums[k]
                if abs(target - total) < abs( target- res):
                    res = total
                
                if total < target:
                    j += 1
                else:
                    k -= 1
                
        return  res