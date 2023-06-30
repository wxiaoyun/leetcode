package leetcode

import (
	"math/rand"
	"time"
)

// https://leetcode.com/problems/k-closest-points-to-origin/

func kClosest(points [][]int, k int) [][]int {
	// partition points into two parts
	// left part is smaller than pivot
	// right part is larger than pivot
	partition := func(points [][]int, l, r int) int {
		// Randomly select a pivot index
		rand.Seed(time.Now().UnixNano())
		pivotIndex := rand.Intn(r-l+1) + l

		// Swap the pivot element with the last element
		points[pivotIndex], points[r] = points[r], points[pivotIndex]
		pivot := points[r]
		i := l
		for j := l; j < r; j++ {
			if distance(points[j]) < distance(pivot) {
				points[i], points[j] = points[j], points[i]
				i++
			}
		}
		points[i], points[r] = points[r], points[i]
		return i
	}

	// quick select
	var quickSelect func(points [][]int, l, r, k int)
	quickSelect = func(points [][]int, l, r, k int) {
		if l >= r {
			return
		}
		p := partition(points, l, r)
		if p == k {
			return
		} else if p < k {
			quickSelect(points, p+1, r, k)
		} else {
			quickSelect(points, l, p-1, k)
		}
	}

	quickSelect(points, 0, len(points)-1, k)

	return points[:k]
}

func distance(point []int) int {
	return point[0]*point[0] + point[1]*point[1]
}
