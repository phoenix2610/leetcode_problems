class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lenght = 0
        counting = False

        for c in s:
            if c != " ":
                if not counting:
                    counting = True
                    lenght = 1

                else:
                    lenght += 1

            else:
                counting = False

        return lenght                         