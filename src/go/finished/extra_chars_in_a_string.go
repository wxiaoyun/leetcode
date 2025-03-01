package leetcode

import "math"

// https://leetcode.com/problems/extra-characters-in-a-string

// LeftOver(i, j) = min from k=i+1 to j-1 (
//   LeftOver(i, k) + LeftOver(k, j)
// )

// Base Case 1: LeftOver(i, j) = 0 if in dict
// Base Case 2: LeftOver(i, i+1) = 1 if not in dict

func minExtraChar(s string, dictionary []string) int {
	N := len(s)

	dp := make([][]int, N+1)
	for i := 0; i < N; i++ {
		dp[i] = make([]int, N+1)
		for j := range dp[i] {
			dp[i][j] = -1
		}
	}

	lookUp := make(map[string]bool)
	for _, w := range dictionary {
		lookUp[w] = true
	}

	var helper func(i, j int) int
	helper = func(i, j int) int {
		if dp[i][j] != -1 {
			return dp[i][j]
		}

		w := s[i:j]
		if exists := lookUp[w]; exists {
			dp[i][j] = 0
			return 0
		}

		if len(w) == 1 {
			dp[i][j] = 1
			return 1
		}

		res := math.MaxInt32
		for k := i + 1; k < j; k++ {
			res = min(res, helper(i, k)+helper(k, j))
		}
		dp[i][j] = res
		return res
	}

	return helper(0, N)
}

// func min(a, b int) int {
// 	if a < b {
// 		return a
// 	}
// 	return b
// }
