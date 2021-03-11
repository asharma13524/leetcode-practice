class Solution:
    def minCostClimbingStairs(self, cost: List[int]):
        if not cost:
            return 0
        # create array to store all costs as we move through array
        dp = [0] * len(cost)
        dp[0] = cost[0]
        # only if array is greater than 2 do we store pos. 1
        if len(cost) >= 2:
            dp[1] = cost[1]
        # build up array looking backwards at prev. stored costs
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        # return minimum of final 2 costs stored
        return min(dp[-1], dp[-2])
