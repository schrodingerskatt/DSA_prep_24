# Problem Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

s = input()
i = 0
n = len(s)
ans = 1
hmp = {}
for j in range(n):
    if s[j] in hmp:
        i = max(hmp[s[j]]+1,i)
    ans = max(ans,j-i+1)
    hmp[s[j]] = j
print(ans)