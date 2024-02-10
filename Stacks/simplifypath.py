# Problem Link : https://leetcode.com/problems/simplify-path/description/

class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split('/')
        stack = []
        for token in tokens:
            if token == "" or token == ".":
                continue
            if token == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(token)
        ans = ""
        while stack:
            ans = "/"+stack.pop()+ans
        if len(ans) == 0:
            ans = "/"
        return ans
