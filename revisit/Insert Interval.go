package leetcode

import "leetcode/util"

// https://leetcode.com/problems/insert-interval/

func insert(intervals [][]int, newInterval []int) [][]int {
	if len(intervals) == 0 {
		return [][]int{newInterval}
	}

	if intervals[0][1] < newInterval[0] {
		return append([][]int{intervals[0]}, insert(intervals[1:], newInterval)...)
	}

	if newInterval[1] < intervals[0][0] {
		return append([][]int{newInterval}, intervals...)
	}

	return insert(intervals[1:], []int{
		util.MinInt(intervals[0][0], newInterval[0]),
		util.MaxInt(intervals[0][1], newInterval[1]),
	})
}

// func insert(intervals [][]int, newInterval []int) [][]int {
// 	output := [][]int{}

// 	if len(intervals) == 0 {
// 		return [][]int{newInterval}
// 	}

// 	if newInterval[1] < intervals[0][0] {
// 		return append([][]int{newInterval}, intervals...)
// 	}

// 	if intervals[len(intervals)-1][1] < newInterval[0] {
// 		return append(intervals, newInterval)
// 	}

// 	for i := 0; i < len(intervals); i++ {
// 		interval := intervals[i]
// 		var next []int = interval

// 		if (interval[0] <= newInterval[0] && newInterval[0] <= interval[1]) ||
// 			(interval[0] <= newInterval[1] && newInterval[1] <= interval[1]) {
// 			next[0] = minInt(intervals[i][0], newInterval[0])
// 			for i < len(intervals) && (intervals[i][1] <= newInterval[1] || intervals[i][0] <= newInterval[1]) {
// 				next[1] = maxInt(intervals[i][1], newInterval[1])
// 				fmt.Println(next)
// 				i++
// 			}
// 			i--
// 		}

// 		output = append(output, next)
// 	}

// 	return output
// }
