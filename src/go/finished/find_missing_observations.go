package leetcode

import "math"

// https://leetcode.com/problems/find-missing-observations/

func missingRolls(rolls []int, mean int, n int) []int {
	totalRolls := len(rolls) + n
	sum := mean * totalRolls
	remaining := sum
	for _, r := range rolls {
		remaining -= r
	}

	if remaining > 6*n || remaining < 1*n {
		return []int{}
	}

	navg := float64(remaining) / float64(n)
	nLow := math.Floor(navg)
	nLowInt := int(nLow)
	lowSum := nLow * float64(n)
	leftOver := float64(remaining) - lowSum
	leftOverInt := int(leftOver)

	res := []int{}
	for i := 0; i < (n - leftOverInt); i++ {
		res = append(res, nLowInt)
	}
	for i := 0; i < leftOverInt; i++ {
		res = append(res, nLowInt+1)
	}
	return res
}
