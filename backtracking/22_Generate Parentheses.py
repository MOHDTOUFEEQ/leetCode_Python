class Solution(object):
    def generateParenthesis(self, n):
        res =[]

        
        def backtracking(left,right,curr):
            if len(curr) == (n*2):
                res.append("".join(curr[:]))
                return
            if left < n:
                curr.append("(")
                backtracking(left+1,right,curr) 
                curr.pop()

            if right < left:
                curr.append(")")
                backtracking(left,right+1,curr) 
                curr.pop()


        backtracking(0,0,[])
        return res