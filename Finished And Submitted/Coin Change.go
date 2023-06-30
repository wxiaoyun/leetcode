package todos

// https://leetcode.com/problems/coin-change/

func coinChange(coins []int, amount int) int {
	dp := make([]int, amount+1)
	for i := range dp {
		// set to max value
		dp[i] = 1 << 31
	}
	// it takes 0 coin to make 0 amount
	dp[0] = 0

	// For each coin and all its previous coins, we check the minimum number of coins needed to make the amount
	for _, c := range coins {
		// for i amount of money and with the current available number of coins
		// we can either not use the current coin (dp[i])
		// or use the current coin (dp[i-c]+1)
		// we take the minimum of the two
		for i := c; i <= amount; i++ {
			dp[i] = min(dp[i], dp[i-c]+1)
		}
	}
	// if the value is still the max value, it means we can't make the amount
	if dp[amount] == 1<<31 {
		return -1
	}
	return dp[amount]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
