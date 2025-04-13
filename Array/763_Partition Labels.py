from collections import Counter
class Solution:
    def partitionLabels(self, s):
        count = Counter(s)
        res = []
        curr = {}
        val = 0
        for i in range(0,len(s)):
            val += 1
            curr[s[i]] = curr.get(s[i],0) + 1
            flag = True
            for left , right in curr.items():
                if right != count[left]:
                    flag = False
            
            if flag is True:
                res.append(val)
                curr = {}
                val = 0
        
        
        return res




# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         count = 0
#         lastIndex = {}
#         output = []
#         end = 0
        
#         for i,j in enumerate(s):
#             lastIndex[j] = i
        
#         for i in range(0,len(s)):
#             count += 1
#             if lastIndex[s[i]] > end:
#                 end = lastIndex[s[i]]
                
#             if i == end:
#                 output.append(count)
#                 count = 0
#                 end = float("-inf")

#         return output