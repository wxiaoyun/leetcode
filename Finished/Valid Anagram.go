package leetcode

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	count := make([]int, 26)
	for i, v := range s {
		count[v-'a']++
		count[t[i]-'a']--
	}

	for _, v := range count {
		if v != 0 {
			return false
		}
	}

	return true
}
