package leetcode

func numTilings(n int) int {
	dp := make([][4]int, n)
	dp[n-1][0] = 1
	dp[n-1][1] = 0
	dp[n-1][2] = 0
	dp[n-1][3] = 1
	return f(0, true, true, dp)
}

func f(index int, t1, t2 bool, dp [][4]int) int {
	if index >= len(dp) {
		return 0
	}

	outputCol := tilesToCol(t1, t2)
	if dp[index][outputCol] != 0 {
		return dp[index][outputCol]
	}

	t3, t4 := detectTiles(index, dp)

	count := 0
	if t1 && t2 && t3 {
		count += f(index+1, false, true, dp) // place L
	}
	if t1 && t2 && t4 {
		count += f(index+1, true, false, dp) // place |^
	}
	if !t1 && t2 && t3 && t4 {
		count += f(index+1, false, false, dp) // _|
	}
	if t1 && !t2 && t3 && t4 {
		count += f(index+1, false, false, dp) // ^|
	}
	if t1 && t2 {
		count += f(index+1, true, true, dp) // |
	}
	if !t1 && !t2 {
		count += f(index+1, true, true, dp) // nothing
	}
	if t1 && t2 && t3 && t4 {
		count += f(index+1, false, false, dp) // =
	}
	if !t1 && t2 && t4 {
		count += f(index+1, true, false, dp) // _
	}
	if t1 && !t2 && t3 {
		count += f(index+1, false, true, dp) // ^
	}

	dp[index][outputCol] = count % 1000000007
	return dp[index][outputCol]
}

func detectTiles(index int, dp [][4]int) (t3, t4 bool) {
	if index == len(dp)-1 {
		return false, false
	}

	return true, true
}

func tilesToCol(t1, t2 bool) int {
	if t1 && t2 {
		return 0
	}

	if t1 {
		return 1
	}

	if t2 {
		return 2
	}

	return 3
}
