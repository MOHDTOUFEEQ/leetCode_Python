from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNoteMap = Counter(ransomNote)
        magazineMap = Counter(magazine)
        
        for char in ransomNoteMap:
            if magazineMap[char] < ransomNoteMap[char]:
                return False

        return True
