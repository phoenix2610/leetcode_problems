class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0
        substrings = []
        freq = defaultdict(int)

        for i,char in enumerate(word):
            if char in "aeiou" :
                if not i or word[i-1] not in "aeiou":
                    jj = j = i 
                    freq.clear()
                freq[char] += 1

                while len(freq) ==5 and all(freq.values()):
                    freq[word[j]] -= 1
                    j += 1
                count += j - jj
        return count  



