class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_count = {}
        consonant_count = {}


        for char in s:
            if char in 'aeiou':
                vowel_count[char] = vowel_count.get(char,0) + 1

            else:
                consonant_count[char]= consonant_count.get(char,0) + 1

        max_vowel = max(vowel_count.values(), default = 0)
        max_consonant= max(consonant_count.values(), default = 0)
            
        return max_vowel + max_consonant