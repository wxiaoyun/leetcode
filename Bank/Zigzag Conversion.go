package leetcode

import (
	"strings"
)

func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}

	builder := strings.Builder{}

	for i := 0; i < numRows; i++ {
		for j := i; j < len(s); {
			if i == 0 || i == numRows-1 {
				builder.WriteByte(s[j])
				j += 2*numRows - 2
			} else {
				builder.WriteByte(s[j])
				j += 2*numRows - 2 - 2*i
				if j < len(s) {
					builder.WriteByte(s[j])
					j += 2 * i
				}
			}
		}
	}

	return builder.String()
}
