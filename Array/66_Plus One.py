class Solution:
    def plusOne(self, digits):
        carry = 1
        
        for i in range(len(digits)-1,-1,-1):
            total  =  digits[i] + carry 
            if total < 10:
                digits[i] = total
                return digits
            else:
                
                digits[i] = int(str(total)[1])
    
                 
        digits = [1] + digits
        
        return digits