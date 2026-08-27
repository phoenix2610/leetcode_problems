class Solution:
    def scoreOfString(self, s: str) -> int:
        output = 0
        temp = []

        for char in s:
            
            temp.append(ord(char))

        for i in range(len(temp)-1):
                current_num = abs(temp[i]- temp[i+1])
                output += current_num

        return output        
