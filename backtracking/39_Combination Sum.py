class Solution:
    def combinationSum(self, candidates, target):
        res = []
        
        def backtracking(curr,total,start):
            if total == target:
                res.append(curr[:])
                return 
            if total > target or start >= len(candidates):
                return

            for i in range(start,len(candidates)):

                curr.append(candidates[i])
                backtracking(curr,total+candidates[i],i)
                curr.pop()
                
        
        backtracking([],0,0)
        
        return res