package leetcode

import (
	"math"
	"slices"
)

func arrayRankTransform(arr []int) []int {
	imt := make([][]int, len(arr))

	for i, n := range arr {
		imt[i] = []int{i, n}
	}

	slices.SortFunc(imt, func(a, b []int) int {
		return a[1] - b[1]
	})

	result := make([]int, len(arr))

	rank := 0
	prev := math.MinInt64
	for _, tpl := range imt {
		if tpl[1] != prev {
			rank++
		}
		result[tpl[0]] = rank
		prev = tpl[1]
	}

	return result
}
