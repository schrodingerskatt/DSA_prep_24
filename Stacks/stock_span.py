# Problem Link : https://leetcode.com/problems/online-stock-span/description/

stock_span = [100, 80, 60, 70, 60, 75, 85]
n = len(stock_span)
stack = [] # it will store pair of (current_price, count of stock prices that are lower than it)
res = [0]*n

for i in range(n):
    span = 1
    while stack and stock_span[i] >= stack[-1][0]:
        span+=stack[-1][1]
        stack.pop()
    stack.append([stock_span[i],span])
    res[i] = span
print(res)

