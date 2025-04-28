class Solution:
    def climbStairs(self, n: int) -> int:
        second = 1
        first = 1
        
        for i in range(n-2,-1,-1):
            res = first + second
            second = first
            first = res
        
        return first