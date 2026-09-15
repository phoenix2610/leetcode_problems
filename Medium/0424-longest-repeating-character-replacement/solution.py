class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        freq= defaultdict(int)
        for right in range(len(s)):
            freq[s[right]] += 1

            if right-left+1 - max(freq.values()) <= k:
                max_len = max(max_len, right-left+1)
                
            else:
                freq[s[left]]  -= 1
                left += 1

        return max_len 