class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        

        for k in range(1,n):
            if n % k == 0:
                pattern = s[:k]

                if pattern * (n // k) == s:
                    return True  
        return False    