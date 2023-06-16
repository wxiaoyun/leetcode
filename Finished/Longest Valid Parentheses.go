package leetcode

func longestValidParentheses(s string) int {
	leftBrackets, rightBrackets, max := 0, 0, 0

	for _, char := range s {
		if char == '(' {
			leftBrackets++
		} else {
			rightBrackets++
		}

		if leftBrackets == rightBrackets && leftBrackets*2 > max {
			max = leftBrackets * 2
		} else if leftBrackets < rightBrackets {
			leftBrackets, rightBrackets = 0, 0
		}
	}

	leftBrackets, rightBrackets = 0, 0

	for i := range s {
		char := s[len(s)-1-i]
		if char == '(' {
			leftBrackets++
		} else {
			rightBrackets++
		}

		if leftBrackets == rightBrackets && leftBrackets*2 > max {
			max = leftBrackets * 2
		} else if leftBrackets > rightBrackets {
			leftBrackets, rightBrackets = 0, 0
		}
	}

	return max
}
