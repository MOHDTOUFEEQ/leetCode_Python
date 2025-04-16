class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res1 =  [-1] * len(nums1)
        res2 =  [-1] * len(nums2)
        stack = []
        for i in range(0,len(nums2)):
            while(stack and nums2[i] > nums2[stack[-1]]):
                index = stack.pop()
                res2[index] = nums2[i]
            
            stack.append(i)
        
        for j in range(0,len(nums1)):
            index = nums2.index(nums1[j])
            res1[j] = res2[index]
                    
        return res1