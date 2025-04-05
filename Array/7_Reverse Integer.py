class Solution:
    def reverse(self, x):
            
        sign = -1 if x<0 else 1
        
        x = abs(x)

        reversed_str = str(x)[::-1]
        reversed_num = int(reversed_str) * sign
        
        print(reversed_num)
        
        if reversed_num > (2**31-1) or reversed_num < - (2**31) :
            return 0

            
        return reversed_num