# Problem Link : https://leetcode.com/problems/baseball-game/description/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if stack and op == "D":
                double = stack[-1]*2
                stack.append(double)
            elif stack and op == "C":
                stack.pop()
            elif stack and op == "+":
                second = stack[-1]
                stack.pop()
                first = stack[-1]
                stack.pop()
                stack.append(first)
                stack.append(second)
                stack.append(first+second)
            else:
                stack.append(int(op))
        total = 0
        while stack:
            val = stack.pop()
            total+=val
        return total
        