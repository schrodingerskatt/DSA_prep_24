# Problem Link : https://www.youtube.com/watch?v=bUSaenttI24&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=16

n = 5
values = [15, 14, 10, 45, 30]
weights = [2, 5, 1, 3, 4]
target = 7
dp = [[0]*(target+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(target+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif weights[i-1] <= j:
            val = j - weights[i-1]
            if dp[i-1][val]+values[i-1] > dp[i-1][j]:
                dp[i][j] = dp[i-1][val]+values[i-1]
            else:
                dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][target])