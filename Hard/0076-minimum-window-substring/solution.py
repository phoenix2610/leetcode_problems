class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        window = {}
        needed = Counter(t)
        left = 0
        formed = 0
        answer = ""

        if len(s) < len(t):
            return ""

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char,0) + 1
            
            if char in needed and window[char] == needed[char]:
                formed += 1

            while formed == len(needed):
                current = s[left:right + 1]

                if answer == "" or len(current) < len(answer):
                    answer = current

                left_char = s[left]
                window[left_char] -=1

                if left_char in needed and window[left_char]< needed[left_char]:
                    formed -= 1

                left += 1
        return answer               

