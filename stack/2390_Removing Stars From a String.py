class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
    
        for i in s:
            if i.isalpha():
                stack.append(i)
            else:
                stack.pop()
                
                
        return ''.join(stack) 