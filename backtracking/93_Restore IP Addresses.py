class Solution:
    def restoreIpAddresses(self, s):
        res = []
        
        def backtracking(curr,index):
            
            if(len(curr) == 4 and index == len(s)):
                res.append(".".join(curr[:]))
                return
            
            if(len(curr)>=4 or index>=len(s)):
                return 
                
            
            for i in range(index,index+3):
                number = s[index:i+1]
                if (index>len(s)) or (len(number) > 1 and number[0] == '0') or int(number)>255:
                    return 
                
                curr.append(s[index:i+1])
                
                backtracking(curr, i+1)
                
                curr.pop()
        
        
        backtracking([],0)
        
        
        return res