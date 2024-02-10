# Problem Link : https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "*" and stack:
                stack.pop()
            else:
                stack.append(char)
        s = ""
        for i in range(len(stack)):
            s+=stack[i]
        return s
        