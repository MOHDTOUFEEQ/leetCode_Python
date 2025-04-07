class Solution(object):
    def isSubsequence(self, s, t):
        if len(t)<len(s):
            return False

        if len(s) == 0 or (len(s) ==0 and len(t) == 0):
            return True
        
        curr = 0
        for i in t:
            if s[curr] == i:
                curr += 1
                if curr == len(s):
                    return True

        
        return False
