# Problem Link : https://leetcode.com/problems/remove-k-digits/description/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k-=1
            stack.append(digit)
        s = stack[:-k] if k else stack # to handle increasing array cases like 12345
        return "".join(s).lstrip('0') or "0"
        