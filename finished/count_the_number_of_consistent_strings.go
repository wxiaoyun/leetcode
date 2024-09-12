package leetcode

// Time: O(max(N, MK)), where N = len(allowed), M = len(words), K = avg str len of words
// Space: O(N)
func countConsistentStrings(allowed string, words []string) int {
	set := make(map[rune]bool)
	for _, c := range allowed {
		set[c] = true
	}

	consistentCount := 0
	for _, w := range words {
		isConsistent := true
		for _, c := range w {
			if in, ok := set[c]; !in || !ok {
				isConsistent = false
				break
			}
		}

		if isConsistent {
			consistentCount++
		}
	}

	return consistentCount
}
