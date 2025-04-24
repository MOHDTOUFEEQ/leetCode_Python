class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        
        for i in range(0,len(s)):
            score = [0]*26
            
            score[ord(s[i])-97] = 1 
            
            for j in range(i+1,len(s)):
                
                score[ord(s[j])-97] += 1 
                
                maxx = max(score)
                minn = min([i for i in score if i > 0])
                
                res += (maxx-minn)
                
        
        
        
        return res