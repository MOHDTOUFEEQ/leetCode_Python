class Solution(object):
    def isAnagram(self, s, t):
        sCounter = {}
        tCounter = {}

        for i,j in zip(s,t):
            if i in sCounter:
                sCounter[i] += 1
            elif i not in sCounter:
                sCounter[i] = 1
            
            
            if j in tCounter:
                tCounter[j] += 1
            elif j not in tCounter:
                tCounter[j] = 1
    
        print(sCounter,tCounter)
        
        return False if sCounter != tCounter or len(s) != len(t) else True