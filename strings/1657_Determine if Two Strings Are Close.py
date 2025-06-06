from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        if set(word1) != set(word2):
            return False    
        
        if sorted(Counter(word1).values()) != sorted(Counter(word2).values()):
            return False 
                
        return True