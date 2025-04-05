class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        curr = s[0]
        lenn = 1
        for i in range(0,len(s)):
            left = i - 1
            right = i + 1
            
            while(left>=0 and right<len(s) and s[left] == s[right]):
                if(right - left + 1 > lenn):
                    curr = s[left:right+1]
                    lenn = right - left + 1
                left -= 1
                right += 1
                
            left = i
            right = i+1
            
            while(left>=0 and right<len(s) and s[left] == s[right]):
                if(right - left + 1 > lenn):
                    curr = s[left:right+1]
                    lenn = right - left + 1
                left -= 1
                right += 1
            
        return curr