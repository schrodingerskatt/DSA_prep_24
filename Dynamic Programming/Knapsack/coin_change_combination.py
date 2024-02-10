# Problem Link : https://leetcode.com/problems/coin-change-ii

# coins = [2, 3, 5] target = 7
# index = [0, 1, 2, 3, 4, 5, 6, 7]
# basically, we chaeck here how many ways are there to make a index amount using coin 2, then 3, then 5 etc.
# for example, we will check using coin 2, in how many ways we can make amount from (2-7)
# using coin 3, in how many ways we can make amount from (3-7)
# using coin 5, in how many ways we can make amount from (5-7)
# since, we are using a coin only once, this ensures we are not getting permutations.

amount = 5
coins = [1, 2, 5]
n = len(coins)
dp = [0]*(amount+1)
dp[0] = 1
for i in range(n):
    for j in range(coins[i],amount+1):
        dp[j]+=dp[j-coins[i]]
print(dp[amount])