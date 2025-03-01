package leetcode

import "strconv"

// https://leetcode.com/problems/decode-ways/

func numDecodings(s string) int {
	if s[0] == '0' {
		return 0
	}

	mem := make([]int, len(s))
	mem[0] = 1

	for i := 1; i < len(s); i++ {
		if isValidLetterTrans(s[i : i+1]) {
			mem[i] += mem[i-1]
		}

		if isValidLetterTrans(s[i-1 : i+1]) {
			if i-2 < 0 {
				mem[i]++
			} else {
				mem[i] += mem[i-2]
			}
		}
	}

	return mem[len(s)-1]
}

func isValidLetterTrans(s string) bool {
	if len(s) == 1 {
		return s != "0"
	}

	// len == 2
	if s[0] == '0' {
		// "06" is invalid
		return false
	}

	num, _ := strconv.Atoi(s)
	return num <= 26
}
