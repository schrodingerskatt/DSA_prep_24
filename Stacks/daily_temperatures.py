# Problem Link : https://leetcode.com/problems/daily-temperatures/description/
# based on next greater element

temperatures = [73,74,75,71,69,72,76,73]
n = len(temperatures)
res = [0]*n
stack = []
stack.append(n-1)

for i in range(n-2, -1, -1):
    while stack and temperatures[i] >= temperatures[stack[-1]]:
        stack.pop()
    if len(stack) == 0:
        res[i] = 0
    else:
        res[i] = stack[-1]-i
    stack.append(i)
print(res)