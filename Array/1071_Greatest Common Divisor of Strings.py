class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        
        for i in range(len(str2)-1,-1,-1):
            val =  str2[:i+1]
            if len(str2) % len(val) == 0 and len(str1) % len(val) == 0 :
                reminder = len(str2) / len(val)
                reminder2 = len(str1) / len(val)
                if val*int(reminder) == str2 and val*int(reminder2) == str1:
                    return val
            
            
        return res