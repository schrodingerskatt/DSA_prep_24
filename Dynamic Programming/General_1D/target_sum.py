# Problem Link : https://leetcode.com/problems/target-sum/description/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}
        def findWays(i,total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i,total) in dp:
                return dp[(i,total)]
            dp[(i,total)] = findWays(i+1,total+nums[i])+findWays(i+1,total-nums[i])
            return dp[(i,total)]
        return findWays(0,0)
        