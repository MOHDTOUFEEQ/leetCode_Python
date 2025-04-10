class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        unique = set(['a','e','i','o','u'])
        
        res = 0
        
        for i in range(k):
            if s[i] in unique:
                res += 1
        
        curr = res  
        for j in range(k,len(s)):
            if s[j-k] in unique:
                curr -= 1
            if s[j] in unique:
                curr += 1
                res = max(res,curr)
        
        return res