class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        output= []

        def depth(openP,closeP, s):
            if openP== closeP and openP + closeP == n*2:
                output.append(s)
                return

            if openP<n:
                depth(openP + 1,closeP,s + '(')

            if closeP<openP:
                depth(openP,closeP+1, s + ")")       


        depth(0,0, '')        
        return output