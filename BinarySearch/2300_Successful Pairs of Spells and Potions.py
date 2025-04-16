import math
class Solution:
    def successfulPairs(self, spells, potions, success: int):
        potions.sort()
        pairs = [0] * len(spells)
        
        for i in range(0,len(spells)):
            left = 0
            right = len(potions) -1 
            length = None

            while(left<=right):
                mid = math.floor((left+right)/2)
                if spells[i] * potions[mid] >= success:
                    length = len(potions) - mid 
                    right = mid - 1
                else:
                    left = mid + 1
                
            if length is not None:
                pairs[i]  = length
        
        return pairs