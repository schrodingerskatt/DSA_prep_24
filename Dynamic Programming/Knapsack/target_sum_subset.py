# Problem Link : https://www.youtube.com/watch?v=tRpkluGqINc&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=11


arr = [4, 2, 7, 1, 3]
target = 10
n = len(arr)
dp = [[False]*(target+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(target+1):
        if i == 0 and j == 0:
            dp[i][j] = True
        elif i == 0:
            dp[i][j] = False
        elif j == 0:
            dp[i][j] = True
        else:
            if dp[i-1][j] == True:
                dp[i][j] = True
            else:
                val = arr[i-1]
                if j >= val:
                    if dp[i-1][j-val] == True:
                        dp[i][j] = True
print(dp[n][target])
