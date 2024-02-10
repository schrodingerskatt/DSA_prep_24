# Problem Link : 

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or stack[-1][0]!= char:
                stack.append([char,1])
            else:
                if stack[-1][1] == k-1:
                    stack.pop()
                else:
                    stack[-1][1]+=1
        ans = ''
        for char,count in stack:
            ans+=char*count
        return ans
        