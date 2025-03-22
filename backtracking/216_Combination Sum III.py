class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtracking(index,summ,curr):
            if(summ == n and len(curr) == k):
                res.append(curr[:])
                return
            if summ>n or len(curr) > k:
                return 
            
            for i in range(index,10):
                if summ+i <=n:
                    curr.append(i)
                    backtracking(i+1,summ+i,curr)
                    curr.pop()
            
        backtracking(1,0,[])
    
        return res