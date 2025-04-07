class Solution(object):
    def romanToInt(self, s):
        val = {'I': 1,'V': 5,'IV':4,'IX':9,'X':10,'XL':40,'XC':90,'CD':400,'CM':900,'L':50,"C":100,'D':500,'M':1000}        
        res = 0
        for i in range(len(s)-1,-1,-1):

            if i+1<len(s) and s[i] == 'I' and s[i+1] == 'V':
                res -= 1
                continue
            elif i+1<len(s) and  s[i] == 'I' and s[i+1] == 'X':
                res -= 1
                continue
            elif i+1<len(s) and  s[i] == 'X' and s[i+1] == 'L':
                res -= 10
                continue
            elif i+1<len(s) and  s[i] == 'X' and s[i+1] == 'C':
                res -= 10
                continue
            elif i+1<len(s) and  s[i] == 'C' and s[i+1] == 'D':
                res -= 100
                continue
            elif i+1<len(s) and   s[i] == 'C' and s[i+1] == 'M':
                res -= 100
                continue
        
            res += val[s[i]]

        return res
        