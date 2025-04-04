class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[] for i in range(numRows) ]
    
        a = 0
        
        while(a<len(s)):
            for i in range(numRows):
                if a>=len(s): break
                matrix[i].append(s[a])
                a += 1
             
            for j in range(numRows-2,0,-1):
                if a>=len(s): break
                matrix[j].append(s[a])
                a += 1
            
        return "".join(["".join(row) for row in matrix])