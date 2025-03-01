package leetcode

import (
	"strconv"
	"strings"
)

// https://leetcode.com/problems/sum-of-digits-of-string-after-convert

func getLucky(s string, k int) int {
	sb := strings.Builder{}
	for _, ch := range s {
		sb.WriteString(strconv.Itoa(int(ch) - 96))
	}
	digits := sb.String()

	for i := 0; i < k; i++ {
		sum := 0
		for _, d := range digits {
			digit, _ := strconv.Atoi(string(d))
			sum += digit
		}
		digits = strconv.Itoa(sum)
	}
	res, _ := strconv.Atoi(digits)
	return res
}
