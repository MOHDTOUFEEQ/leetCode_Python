class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
          return 0 
        zero = 0
        first = 1
        
        for i in range(2,n+1):
            res = first + zero
            zero = first
            first = res
        
        
        return first