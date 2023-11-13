package leetcode

import (
	"slices"
)

// https://leetcode.com/problems/sort-vowels-in-a-string/

func sortVowels(s string) string {
	output := make([]rune, 0, len(s))
	vowels := make([]rune, 0, len(s))

	for _, char := range s {
		if isVowel(char) {
			output = append(output, '0')
			vowels = append(vowels, char)
		} else {
			output = append(output, char)
		}
	}

	slices.Sort(vowels)

	cur := 0
	for i, char := range output {
		if cur >= len(vowels) {
			break
		}

		if char == '0' {
			output[i] = vowels[cur]
			cur++
		}
	}

	return string(output)
}

func isVowel(c rune) bool {
	switch c {
	case 'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U':
		return true
	default:
		return false
	}
}
