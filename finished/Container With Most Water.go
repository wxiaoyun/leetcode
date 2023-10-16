package leetcode

import "math"

// func maxArea(height []int) int {
// 	maxVol := 0.0
// 	for i, l := range height {
// 		for j := i; j < len(height); j++ {
// 			minHeight := math.Min(float64(l), float64(height[j]))
// 			maxVol = math.Max(maxVol, minHeight*float64(j-i))
// 		}
// 	}
// 	return int(maxVol)
// }
func maxArea(height []int) int {
	maxVol := 0.0
	l := 0
	r := len(height) - 1

	for l < r {
		currVol := float64(r-l) * math.Min(float64(height[l]), float64(height[r]))
		maxVol = math.Max(maxVol, currVol)

		if height[l] < height[r] {
			l++
		} else {
			r--
		}
	}

	return int(maxVol)
}
