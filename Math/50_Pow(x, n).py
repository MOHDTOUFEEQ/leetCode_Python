class Solution:
    def myPow(self, x, n):
        base = abs(x)
        power = abs(n)
        
        res = base ** power
        
        if n < 0 :
            res = 1/res
        
        if n<0 or x<0:
            if n<0 and x<0 :
                return res
            else:
                return -res
        
        return res