# Problem Link : https://leetcode.com/problems/longest-palindromic-substring/description/

s = input()
n = len(s)
dp = [[False]*n for _ in range(n)]

for g in range(n):
    i = 0
    for j in range(g,n):
        if g == 0:
            dp[i][j] = True
        elif g == 1:
            if s[i] == s[j]:
                dp[i][j] = True
            else:
                dp[i][j] = False
        else:
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = False
        i+=1

longest = 0
ans = ""

for i in range(n):
    for j in range(n):
        if dp[i][j] == True:
            if longest < j-i+1:
                longest = j-i+1
                ans = s[i:j+1]
print(ans)
        

