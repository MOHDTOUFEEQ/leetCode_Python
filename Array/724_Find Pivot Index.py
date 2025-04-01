class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = []
        sumRight = [0 for i in nums]
        leftCurr = 0
        
        for obj in nums:
            sumLeft.append(leftCurr)
            leftCurr += obj
        
        rightCurr = 0
        rightIndex = len(nums)-2
        for i in range(len(nums)-1,-1,-1):
            sumRight[rightIndex] = rightCurr+nums[i]
            rightCurr += nums[i]
            rightIndex -= 1
    
        sumRight[-1] = 0    
        for i in range(len(sumLeft)):
            if(sumLeft[i]==sumRight[i]):
                return i 
        
        return -1 