package leetcode

import "sort"

func permuteUnique(nums []int) [][]int {
	sort.Ints(nums) // sort the array for duplicate checking
	results := make([][]int, 0)
	backtrack(&results, nums, []int{}, make([]bool, len(nums)))
	return results
}

func backtrack(results *[][]int, nums, current []int, used []bool) {
	if len(current) == len(nums) { // reached a valid perm
		temp := make([]int, len(current))
		copy(temp, current)
		*results = append(*results, temp)
		return
	}

	for i, val := range nums {
		if used[i] {
			continue
		}

		if i > 0 && nums[i] == nums[i-1] && !used[i-1] {
			continue
		}

		used[i] = true
		current = append(current, val)
		backtrack(results, nums, current, used)
		current = current[0 : len(current)-1] // backtrack
		used[i] = false
	}
}

// func permuteUnique(nums []int) [][]int {
//   dp := [][]int{[]int{nums[0]}}

//   for i, num := range nums {
//     if i == 0 {
//       continue;
//     }

//     newDp := make([][]int, 0)

//     for _, prevPerm := range dp {
//       for i := 0; i <= len(prevPerm); i++ {
//         newPerm := make([]int, len(prevPerm)+1)
//         copy(newPerm[0:i],prevPerm[0:i])
//         newPerm[i] = num
//         copy(newPerm[i+1:], prevPerm[i:])
//         newDp = append(newDp, newPerm)
//       }
//     }

//     dp = newDp
//   }

//   make
//   fmt.Println(dp)

//   return dp
// }
