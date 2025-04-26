class Solution:
    def partition(self, s):
        res = []
        
        def backtracking(curr,index):
            if index == len(s):
                res.append(curr[:])
                return
            
            if index >= len(s):
                return 
            
            for i in range(index,len(s)):
                val = s[index:i+1]
                if val == val[::-1]:
                    curr.append(val)
                    backtracking(curr,i+1)
                    curr.pop()
        
        
        backtracking([],0)

        return res