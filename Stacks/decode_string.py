# Problem Link : https://leetcode.com/problems/decode-string/description/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1]!="[":
                    substr = stack.pop()+substr
                stack.pop()
                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop()+digit
                stack.append(int(digit)*substr)
        return "".join(stack)