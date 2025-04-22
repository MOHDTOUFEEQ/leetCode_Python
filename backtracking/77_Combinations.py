class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtracking(curr,number):
            if len(curr) == k:
                res.append(curr[:])
                return 
            
            
            for i in range(number, n + 1):
                curr.append(i)
                backtracking(curr,i+1)
                curr.pop()
        
        
        
        
        backtracking([],1)
        
        return res