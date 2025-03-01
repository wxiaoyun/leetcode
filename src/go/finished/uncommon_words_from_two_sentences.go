package leetcode

import "strings"

func uncommonFromSentences(s1 string, s2 string) []string {
	words_a := strings.Split(s1, " ")
	words_b := strings.Split(s2, " ")

	dict_a := make(map[string]int)
	dict_b := make(map[string]int)

	for _, w := range words_a {
		dict_a[w]++
	}
	for _, w := range words_b {
		dict_b[w]++
	}

	uncommon := make([]string, 0, len(words_a))
	for w, f := range dict_a {
		if f != 1 {
			continue
		}
		if ff, ok := dict_b[w]; ff == 0 || !ok {
			uncommon = append(uncommon, w)
		}
	}
	for w, f := range dict_b {
		if f != 1 {
			continue
		}
		if ff, ok := dict_a[w]; ff == 0 || !ok {
			uncommon = append(uncommon, w)
		}
	}

	return uncommon
}
