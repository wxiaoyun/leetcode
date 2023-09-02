package leetcode

import (
	"fmt"
	"strings"
)

func lengthOfLastWord(s string) int {
	words := strings.Split(strings.Trim(s, " "), " ")

	result := ""
	for i := len(words) - 1; i >= 0; i-- {
		fmt.Println(words[i])
		if words[i] != "" || words[i] != " " {
			result = words[i]
			break
		}
	}

	return len(result)
}
