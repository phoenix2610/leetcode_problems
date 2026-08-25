class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        main_string = s + s
        

        if goal in main_string and len(s) == len(goal):
            return True
        return False    