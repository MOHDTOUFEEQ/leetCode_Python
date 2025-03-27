class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for i in asteroids:
            while(len(stack)>0 and i < 0 and stack[-1] > 0):
                if abs(stack[-1]) > abs(i):
                    i = 0
                    break
                
                elif abs(stack[-1]) == abs(i):
                    stack.pop()
                    i = 0
                    break
                
                elif  abs(stack[-1]) < abs(i):
                    stack.pop()
            
            if i != 0:
                stack.append(i)
        
        return stack