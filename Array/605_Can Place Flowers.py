class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            else:
                if (i > 0 and flowerbed[i-1] == 1) or (i<len(flowerbed)-1 and flowerbed[i+1] == 1):
                    continue
                else:
                    flowerbed[i] = 1
                    n -= 1
                    
        if n <= 0:
            return True
        
        return False