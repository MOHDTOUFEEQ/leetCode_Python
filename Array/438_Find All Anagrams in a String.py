from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s)<len(p):
            return []
        pCount = Counter(p)
        sCount = Counter(s[:len(p)])
        
        res = []
        if pCount == sCount:
            res.append(0)
        

        for i in range(len(p),len(s)):
            sCount[s[i-len(p)]] -= 1
            if sCount[s[i-len(p)]] == 0:
                del sCount[s[i-len(p)]]
            
            if s[i] in sCount:
                sCount[s[i]] += 1
            else:
                sCount[s[i]] = 1
        
            if pCount == sCount:
                res.append(i-len(p)+1)
            
        
        
        return res