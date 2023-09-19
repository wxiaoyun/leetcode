package leetcode

import "math"

func minPathSum(grid [][]int) int {
	// initialise
	dp := make([][]int, len(grid))
	for i := range dp {
		dp[i] = make([]int, len(grid[0]))
		for j := range dp[i] {
			dp[i][j] = -1
		}
	}

	dp[0][0] = grid[0][0]

	return helper(grid, dp, len(grid)-1, len(grid[0])-1)
}

func helper(grid, dp [][]int, r, c int) int {
	if r < 0 || c < 0 {
		return math.MaxInt64
	}

	if dp[r][c] >= 0 {
		return dp[r][c]
	}

	leftGridPathSum := helper(grid, dp, r, c-1)
	topGridPathSum := helper(grid, dp, r-1, c)

	dp[r][c] = min(leftGridPathSum, topGridPathSum) + grid[r][c]
	return dp[r][c]
}

// func min(a, b int) int {
// 	if a < b {
// 		return a
// 	}
// 	return b
// }
