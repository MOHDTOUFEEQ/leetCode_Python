class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        curr = 0
        for i in gain:
            curr = curr + i
            res = max(res,curr)
            
        return res