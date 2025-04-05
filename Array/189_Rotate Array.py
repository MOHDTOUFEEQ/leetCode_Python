class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        
        if length == k or k % length == 0:
            return nums
            
        k = k % length
        res = length - k 
            
        temp = nums[res:]
        nums[res : ] = []
        nums[0:0] =  temp
        



        return nums