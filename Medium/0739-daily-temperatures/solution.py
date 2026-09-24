class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    output[i] = j-i
                    break

        return output


