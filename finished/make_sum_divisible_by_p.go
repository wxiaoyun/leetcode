package leetcode

func minSubarray(nums []int, p int) int {
	N := len(nums)
	totalSum := 0

	for _, n := range nums {
		totalSum = (totalSum + n) % p
	}

	if totalSum == 0 {
		return 0
	}

	modIndex := map[int]int{
		0: -1,
	}

	current := 0
	minLen := N
	for i, n := range nums {
		current = (current + n) % p
		complement := (current - totalSum + p) % p

		if j, ok := modIndex[complement]; ok {
			minLen = min(minLen, i-j)
		}

		modIndex[current] = i
	}

	if minLen == N {
		return -1
	}

	return minLen
}

// O(n^2)
// func minSubarray(nums []int, p int) int {
//     prefixSum := make([]int, len(nums)+1)
//     prefixSum[0] = 0
//     for i, num := range nums {
//       prefixSum[i+1] = prefixSum[i] + num
//     }

//     total := prefixSum[len(nums)]
//     minLen := int(math.MaxInt64)
//     for i := 0; i < len(nums); i++ {
//       for j := i; j <= len(nums); j++ {
//         length := j - i;
//         if length >= minLen {
//           break
//         }

//         subTotal := prefixSum[j] - prefixSum[i]
//         sum := total - subTotal
//         if sum % p == 0 {
//           minLen = min(minLen, length)
//         }
//       }
//     }

//     if minLen == len(nums) {
//       return -1
//     }

//     return minLen
// }
