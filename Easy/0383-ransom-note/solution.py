class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        main_hash = {}


        for c in magazine:
            main_hash[c] = main_hash.get(c, 0) + 1


        for c in ransomNote:
            if c not in main_hash: 
                return False

            main_hash[c] -= 1

            if main_hash[c]==0:
                
                del main_hash[c]  
                  
        return True                   