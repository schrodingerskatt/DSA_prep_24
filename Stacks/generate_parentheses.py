# Problem Link : https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        max_size = 2*n
        ans = []
        def isvalid(s):
            stack = []
            for i in range(len(s)):
                if s[i] == ')' and len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s[i])
            if len(stack) == 0:
                return True
            return False
        def permutations(i,curstr):
            if i == max_size:
                if isvalid(curstr):
                    ans.append(curstr+'')
                    return
                else:
                    return
            permutations(i+1,curstr+'(')
            permutations(i+1,curstr+')')
        permutations(0,"")
        return ans
        