class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n

        dp = [0,1,2]

        for i in range(3, n+1):
            ways = dp[i-1]+dp[i-2]
            dp.append(ways)

        return dp[n] 
