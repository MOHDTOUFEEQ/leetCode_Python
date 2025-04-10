class Solution:
    def wordPattern(self, pattern, s):
        s = s.split(" ")
        pattern = list(pattern)
        if len(s) != len(pattern):
            return False
            
        patternMap = {}
        sMap = {}
        
        for i,j in zip(s,pattern):
            if i in patternMap:
                if j != patternMap[i]:
                    return False
            else:
               patternMap[i] = j
               
            if j in sMap:
                if i != sMap[j]:
                    return False
            else:
               sMap[j] = i
               
             
                
        
        return True