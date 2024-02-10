# Problem Link : https://leetcode.com/problems/perfect-squares/description

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2,n+1):
            j = 1
            min_count = float("infinity")
            while j*j <= i:
                rem = i-j*j
                if dp[rem] < min_count:
                    min_count = dp[rem]
                j+=1
            dp[i] = min_count+1
        return dp[n]
        
        
                