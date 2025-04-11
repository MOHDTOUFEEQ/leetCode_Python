class Solution:
    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []
        mapping = {"2":['a','b','c'],"3":['d','e','f'],"4":['g','h','i'],
        "5":['j','k','l'],"6":['m','n','o'],"7":['p','q','r','s'],"8":['t','u','v'],"9":['w','x','y','z']}
        res = []
        
        def backtracking(index, curr):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return 
        
            arr = mapping[digits[index]]
            
            for i in range(0,len(arr)):
                curr.append(arr[i])
                backtracking(index+1,curr)
                curr.pop()
                
        
        backtracking(0,[])
        return res