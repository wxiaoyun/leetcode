package leetcode

// https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k

func canArrange(arr []int, k int) bool {
	count := make([]int, k)

	for _, n := range arr {
		grp := n % k
		grp = (grp + k) % k
		count[grp]++
	}

	if count[0]%2 != 0 {
		return false
	}

	for i := 1; i < k; i++ {
		j := k - i
		if count[i] != count[j] {
			return false
		}
	}

	return true
}
