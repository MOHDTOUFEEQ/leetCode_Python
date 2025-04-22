class Solution:
    def isHappy(self, n: int) -> bool:
        unique = set()
        
        a = str(n)
        summ = 0
        
        while (summ not in unique):
    
            unique.add(summ)
            
            summ = 0
            for i in a:
                summ += (int(i)**2)
            
            a = str(summ)
            
            if summ == 1:
                return True
            
    
        return False