package leetcode

// https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

func findKthNumber(n int, k int) int {
	cur := 1
	k -= 1

	for k > 0 {
		steps := countSteps(n, cur, cur+1)
		if steps <= k {
			cur++
			k -= steps
		} else {
			cur *= 10
			k--
		}
	}

	return cur
}

func countSteps(n, p1, p2 int) int {
	steps := 0
	for p1 <= n {
		steps += min(n+1, p2) - p1
		p1 *= 10
		p2 *= 10
	}
	return steps
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// TLE
// func findKthNumber(n int, k int) int {
//     count := 0
//     var helper func(int) int
//     helper = func(accum int) int {
//       if accum > n {
//         return -1
//       }

//       count++
//       if count == k {
//         return accum
//       }

//       for i := 0; i < 10; i++ {
//         if result := helper(accum*10+i); result != -1 {
//           return result
//         }
//       }

//       return -1
//     }

//     result := -1
//     for i := 1; i < 10; i++ {
//       if result = helper(i); result != -1 {
//         return result
//       }
//     }
//     return result
// }
