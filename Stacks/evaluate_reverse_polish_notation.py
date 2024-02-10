# Problem Link : https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def evaluate(a,b,op):
            if op == "+":
                return a+b
            if op == "-":
                return a-b
            if op == "*":
                return a*b
            if op == "/":
                return int(a / b) 
            return 0
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                second = stack[-1]
                stack.pop()
                first = stack[-1]
                stack.pop()
                solve = evaluate(first,second,token)
                stack.append(solve)
            else:
                stack.append(int(token))
        return stack[-1]

        