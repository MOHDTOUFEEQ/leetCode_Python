class Solution(object):
    def partitionString(self, s):
        res = 1
        setting = set()
        
        for i in s:
            if i in setting:
                res += 1
                setting = set()
                setting.add(i)
            else:
                setting.add(i)
            
        
        return res
        