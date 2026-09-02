class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        chars = Counter(text)

        return min(chars[k]//v for k,v in {'b':1, 'a':1, 'l':2, 'o':1, 'n':1}.items())