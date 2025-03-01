package leetcode

// Time: O(N + M), where N = len(arr), M = len(queries)
// Space: O(N)
func xorQueries(arr []int, queries [][]int) []int {
	N := len(arr)
	prefixXor := make([]int, N)
	prefixXor[0] = arr[0]
	postfixXor := make([]int, N)
	postfixXor[N-1] = arr[N-1]

	for i := 1; i < N; i++ {
		prefixXor[i] = prefixXor[i-1] ^ arr[i]
		j := N - i - 1
		postfixXor[j] = postfixXor[j+1] ^ arr[j]
	}

	totalXor := 0
	for _, num := range arr {
		totalXor ^= num
	}

	M := len(queries)
	result := make([]int, M)
	for i := 0; i < M; i++ {
		res := totalXor
		q := queries[i]
		left := q[0]
		right := q[1]

		if left > 0 {
			res ^= prefixXor[left-1]
		}
		if right < N-1 {
			res ^= postfixXor[right+1]
		}
		result[i] = res
	}

	return result
}
