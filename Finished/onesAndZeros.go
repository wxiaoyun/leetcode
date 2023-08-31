package leetcode

func findMaxForm(strs []string, m int, n int) int {
	// 2d dp array for storing the possible subsets
	// dp[i][j] => largest subset of strs such that there is at most i '0's and j '1's
	dp := make([][]int, 0, m+1)
	for i := 0; i < m+1; i++ {
		dp = append(dp, make([]int, n+1))
	}

	for _, str := range strs {
		zeros, ones := onesAndZeros(str)

		for i := m; i-zeros >= 0; i-- {
			for j := n; j-ones >= 0; j-- {
				dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
			}
		}
	}

	return dp[m][n]
}

func onesAndZeros(str string) (int, int) {
	zeros, ones := 0, 0

	for _, char := range str {
		if char == '0' {
			zeros++
		}
		if char == '1' {
			ones++
		}
	}

	return zeros, ones
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
