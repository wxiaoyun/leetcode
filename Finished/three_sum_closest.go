package leetcode

import (
	"math"
	"sort"
)

func threeSumClosest(nums []int, target int) int {
	n := len(nums)
	// Sort the input array to use the two-pointer technique
	sort.Ints(nums)

	closestSum := nums[0] + nums[1] + nums[2]

	for i := 0; i < n-2; i++ {
		left := i + 1
		right := n - 1

		for left < right {
			sum := nums[i] + nums[left] + nums[right]

			if Abs(target-sum) < Abs(target-closestSum) {
				closestSum = sum
			}

			if sum < target {
				left++
			} else if sum > target {
				right--
			} else {
				// If the sum is equal to the target, we found the closest sum possible
				return sum
			}
		}
	}

	return closestSum
}

func Abs(a int) int {
	return int(math.Abs(float64(a)))
}

// func threeSumClosest(nums []int, target int) int {
// 	var closestSoFar = nums[0] + nums[1] + nums[2]
// 	for i := 0; i < len(nums); i++ {
// 		for j := 0; j < len(nums); j++ {
// 			for k := 0; k < len(nums); k++ {
// 				if i != j && i != k && j != k {
// 					difference := Abs(target, nums[i]+nums[j]+nums[k])
// 					if difference < closestSoFar {
// 						closestSoFar = nums[i] + nums[j] + nums[k]
// 					}
// 				}
// 			}
// 		}
// 	}
// 	return closestSoFar
// }

// func Abs(a, b int) int {
// 	if a-b < 0 {
// 		return b - a
// 	}
// 	return a - b
// }
