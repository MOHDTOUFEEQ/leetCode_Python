class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtracking(index,curr):
            if index  == len(nums):
                res.append(curr[:])
                return 
            
            backtracking(index+1,curr)
            
            curr.append(nums[index])
            backtracking(index+1,curr)
            curr.pop()
            
        
        
        backtracking(0,[])
        return res