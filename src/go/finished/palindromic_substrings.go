package leetcode

// https://leetcode.com/problems/palindromic-substrings/

func countSubstrings(s string) int {
	count := 1

	helper := func(i, j int) {
		for i >= 0 && j < len(s) && s[i] == s[j] {
			count++
			i--
			j++
		}
	}

	for i := 1; i < len(s); i++ {
		helper(i, i)
		helper(i-1, i)
	}

	return count
}
