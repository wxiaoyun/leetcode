package leetcode

func longestPalindrome(s string) string {
	answer := ""
	for i := range s {
		answer1 := expand(s, i, i)
		answer2 := expand(s, i, i+1)

		if len(answer1) > len(answer) {
			answer = answer1
		}

		if len(answer2) > len(answer) {
			answer = answer2
		}
	}

	return answer
}

func expand(s string, l int, r int) string {
	if l < 0 || r >= len(s) {
		return ""
	}
	for l >= 0 && r < len(s) && s[l] == s[r] {
		l -= 1
		r += 1
	}
	return s[l+1 : r]
}
