from collections import Counter
from functools import reduce
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        duplicate = [Counter(word) for word in words]
        common = reduce(lambda x, y: x & y, duplicate)

        return list(common.elements())


