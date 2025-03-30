class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a','e','i','o',"u"])
        arr = []
        
        for val in s:
            if val.lower() in vowels:
                arr.append(val)
        
        right = len(arr)-1
        res = ""
        
        for i in range(0,len(s)):
            if s[i].lower() in vowels:
                res += arr[right]
                right -= 1
            else:
                res += s[i] 
                
        return res
    
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         vowels = set(['a', 'e', 'i', 'o', 'u']) 
#         res = list(s)
#         left = 0
#         right = len(s)-1
        
#         while(left<right):
#             while(left <right and res[left].lower() not in vowels):
#                 left += 1
            
#             while(left <right and res[right].lower() not in vowels):
#                 right -= 1

#             res[left],res[right] = res[right],res[left]
#             left += 1
#             right -= 1

#         return "".join(res)