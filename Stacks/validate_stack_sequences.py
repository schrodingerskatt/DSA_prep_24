# Problem Link : https://leetcode.com/problems/validate-stack-sequences/description/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        i = 0
        j = 0
        stack = []
        while i < n and j < n:
            stack.append(pushed[i])
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j+=1
            i+=1
        return not stack
        