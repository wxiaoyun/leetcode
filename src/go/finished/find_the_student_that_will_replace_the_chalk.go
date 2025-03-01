package leetcode

// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

// Time O(n + logn) = O(n)
// Space O(n)
func chalkReplacer(chalk []int, k int) int {
	prefixSum := []int{}
	sum := 0
	for _, c := range chalk {
		sum += c
		prefixSum = append(prefixSum, sum)
	}

	remainder := k % sum

	l, r := 0, len(chalk)
	for l < r {
		m := l + (r-l)/2
		pSum := prefixSum[m]

		if pSum <= remainder {
			l = m + 1
		} else {
			r = m
		}
	}

	return r
}

// Time O(2n) = O(n)
// Space O(1)
// func chalkReplacer(chalk []int, k int) int {
//     sum := 0
//     for _, c := range chalk {
//       sum += c
//     }

//     remainder := k % sum
//     for i, c := range chalk {
//       if remainder < c {
//         return i
//       }
//       remainder -= c
//     }

//     return -1
// }
