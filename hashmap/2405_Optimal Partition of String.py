class Solution:
    def partitionString(self, s: str) -> int:
        unique = set()
        res = 1
        for i in s:
            if i in unique:
                res += 1
                unique.clear()
                unique.add(i)
            else:
                unique.add(i)
                
        
        
        return res