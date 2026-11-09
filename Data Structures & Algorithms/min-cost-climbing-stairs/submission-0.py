class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        dp = [0, 0]

        for i in range(2, n + 1):
            one_step = dp[i - 1] + cost[i - 1]
            two_steps = dp[i - 2] + cost[i - 2]

            if one_step < two_steps:
                dp.append(one_step)
            else:
                dp.append(two_steps)

        return dp[n]