package leetcode

import (
	"math"
	"sort"
	"strconv"
	"strings"
)

// Time: O(nlogn), bounded by sort
// Space: O(n)
func findMinDifference(timePoints []string) int {
	times := make([]int, 0, len(timePoints)*2)

	oneDay := 24 * 60
	for _, tp := range timePoints {
		t := convTime(tp)
		times = append(times, t)
		times = append(times, t+oneDay)
	}

	sort.Ints(times)

	minDif := int(math.MaxInt32)
	for i := 1; i < len(times); i++ {
		minDif = min(minDif, abs(times[i-1]-times[i]))
	}

	return minDif
}

func convTime(t string) int {
	splits := strings.Split(t, ":")
	hrs := splits[0]
	min := splits[1]

	hours, err := strconv.Atoi(hrs)
	if err != nil {
		panic(err)
	}

	minutes, err := strconv.Atoi(min)
	if err != nil {
		panic(err)
	}

	return hours*60 + minutes
}

// func min(a, b int) int {
// 	if a < b {
// 		return a
// 	}
// 	return b
// }

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
