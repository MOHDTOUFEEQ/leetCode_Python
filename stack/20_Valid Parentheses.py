class Solution(object):
    def isValid(self, s):
        mapp = {"}":"{",")":"(","]":"["}
        stack = []
        for i in s:
            if i in mapp:
                if len(stack) > 0 and stack[-1] == mapp[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            
        return False if len(stack)>0 else True
