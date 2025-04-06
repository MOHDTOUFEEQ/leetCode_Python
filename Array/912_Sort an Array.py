import math
class Solution(object):
    def sorting(self,arr1,arr2):
        res = []
        i = 0
        j = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        # Add remaining elements
        if i < len(arr1):
            res += arr1[i:]
        if j < len(arr2):
            res += arr2[j:]

        return res

    def sortArray(self, nums):
        if len(nums) == 1:
            return nums
        
        half = int(math.floor(len(nums)/2))
        leftArr = self.sortArray(nums[:half])
        rightArr = self.sortArray(nums[half:])
        
        return self.sorting(leftArr, rightArr)
