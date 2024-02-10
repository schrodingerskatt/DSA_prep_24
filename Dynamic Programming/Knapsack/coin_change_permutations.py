# Problem Link : https://leetcode.com/problems/combination-sum-iv

nums = [1,2,3]
target = 4

# so, basically we will pick every target value from [0 to 4] and check in what ways they can be
# written using all the coins that are smaller than the target value
# since, all the coins will be using for every particular amount, we will get a permutation
# for eg : if target is 5, for coin 2 we will get 1 i.e. [2,3], then at coin 3 we will get 2. i.e.
# [3,2], total = [2,3],[3,2]

dp = [0]*(target+1)
dp[0] = 1

for i in range(target+1):
    for j in range(len(nums)):
        if nums[j] <= i:
            dp[i]+=dp[i-nums[j]]
print(dp[target])