import math
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        low = 1
        high = max(piles)
        res = None
        def helper(index):
            count = h
            for j in range(0,len(piles)):
                count -= math.ceil((piles[j] / index))
                
            if count<0:        
                return False
            else:
                return True
                
        while(low<=high):
            mid = math.floor((low+high)/2)
            result = helper(mid)
            if result is True:
                res = mid
                high = mid - 1
            else:    
                low = mid + 1
                
    
        return res