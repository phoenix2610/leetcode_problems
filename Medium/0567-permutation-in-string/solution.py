from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        w = len(s1)
        
        if len(s1) > len(s2):
            return False

        for i in range(len(s2)):
            if s2[i] in counter:
                counter[s2[i]] -=1

            if i >= w and s2[i-w] in counter:
                 counter[s2[i-w]] +=1

            if all([counter[i]==0 for i in counter]):
                return True

        return False            