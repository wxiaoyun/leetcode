package leetcode

// https://leetcode.com/problems/climbing-stairs/

func minCostClimbingStairs(cost []int) int {
	dp := make([]int, len(cost)+1)
	dp[0] = 0
	dp[1] = 0

	for i := 2; i < len(cost)+1; i++ {
		dp[i] = min(
			dp[i-1]+cost[i-1],
			dp[i-2]+cost[i-2],
		)
	}

	return dp[len(cost)]
}

// func min(a, b int) int {
// 	if a < b {
// 		return a
// 	}
// 	return b
// }

// T(i) = min(
//   T(i-1) + cost(i-1),
//   T(i-2) + cost(i-2),
// )
