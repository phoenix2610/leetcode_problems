class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        alphabets = set()

        for char in sentence: 
            alphabets.add(char)
         
        return len(alphabets) == 26
