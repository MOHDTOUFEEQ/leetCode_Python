class Solution:
    def findDifference(self, nums1, nums2):
        res1 = []
        res1Set = set(nums1)
        res2Set = set(nums2)
        res2 = []

        for i in nums1:
            if i not in res2Set:
                res1.append(i)
                
        for j in nums2:
            if j not in res1Set:
                res2.append(j)
        
        return [list(set(res1)),list(set(res2))]