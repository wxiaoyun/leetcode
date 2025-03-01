package leetcode

import "fmt"

func generateParenthesis(n int) []string {
	if n == 1 {
		return []string{"()"}
	}

	previous := generateParenthesis(n - 1)
	current := map[string]struct{}{}

	for _, paren := range previous {
		// current[fmt.Sprintf("%s()", paren)] = struct{}{}
		// current[fmt.Sprintf("()%s", paren)] = struct{}{}
		// current[fmt.Sprintf("(%s)", paren)] = struct{}{}
		for i := 0; i < len(paren); i++ {
			str := fmt.Sprintf("%s()%s", paren[:i], paren[i:])
			current[str] = struct{}{}
		}
	}

	output := []string{}
	for paren := range current {
		output = append(output, paren)
	}

	return output
}
