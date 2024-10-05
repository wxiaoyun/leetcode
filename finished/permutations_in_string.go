package leetcode

func checkInclusion(s1 string, s2 string) bool {
	s1Map := make([]int, 26)
	for _, c := range s1 {
		s1Map[int(c-'a')]++
	}

	s2Map := make([]int, 26)
	// Invariant: s2Map should be a subset of s1Map
	// Expand if s2Map is a subset of s1Map
	// Shrink if s2Map is not a subset of s1Map
	i := 0
	for _, c := range s2 {
		s2Map[int(c-'a')]++

		res := compMap(s1Map, s2Map)
		for res < 0 {
			s2Map[int(rune(s2[i])-'a')]--
			i++
			res = compMap(s1Map, s2Map)
		}

		if res == 0 {
			return true
		}
	}

	return false
}

// Returns -1 if any value of B is larger than A
// Returns 0 if all values of B is equal to A
// Returns 1 otherwise
func compMap(a, b []int) int {
	allEqual := true
	for i, aFreq := range a {
		if aFreq < b[i] {
			return -1
		}
		if aFreq > b[i] {
			allEqual = false
		}
	}

	if allEqual {
		return 0
	}
	return 1
}
