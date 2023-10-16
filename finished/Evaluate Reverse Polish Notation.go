package leetcode

// https://leetcode.com/problems/evaluate-reverse-polish-notation/

type stack[T any] []T

func (s *stack[T]) push(n T) {
	*s = append(*s, n)
}

func (s *stack[T]) pop() T {
	n := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return n
}

func stringToInt(s string) int {
	if s[0] == '-' {
		return -stringToInt(s[1:])
	}
	n := 0
	for _, c := range s {
		n = n*10 + int(c-'0')
	}
	return n
}

func isNum(token string) bool {
	return token != "+" && token != "-" && token != "*" && token != "/"
}

func operate(num1, num2 int, operator string) int {
	switch operator {
	case "+":
		return num1 + num2
	case "-":
		return num1 - num2
	case "*":
		return num1 * num2
	case "/":
		return num1 / num2
	default:
		return -1
	}
}

func evalRPN(tokens []string) int {
	stack := stack[int]{}

	for _, token := range tokens {
		if isNum(token) {
			stack.push(stringToInt(token))
		} else {
			num1 := stack.pop()
			num2 := stack.pop()
			stack.push(operate(num2, num1, token))
		}
	}
	return stack.pop()
}
