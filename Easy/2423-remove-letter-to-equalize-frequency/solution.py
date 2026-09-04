from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counts = Counter(word)
        for char in list(counts.keys()):
            counts[char] -= 1
            if counts[char] == 0:
                del counts[char]
                
            if len(set(counts.values())) == 1:
                return True
                
            counts[char] += 1
            
        return False