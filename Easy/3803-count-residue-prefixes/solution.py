class Solution:
    def residuePrefixes(self, s: str) -> int:
        
        count = 0
        seen = set()

        for i,char in enumerate(s):
            seen.add(char)

            if len(seen) == (i + 1)  % 3:
                count += 1     


        return count                            
