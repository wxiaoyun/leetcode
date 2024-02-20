package leetcode

func lengthOfLongestSubstring(s string) int {
	lastSeen := make(map[byte]int)
	max := 0

	for left, right := 0, 0; right < len(s); right++ {
		nextChar := s[right]
		if lastSeenIndex, ok := lastSeen[nextChar]; ok && left <= lastSeenIndex {
			left = lastSeenIndex + 1
		} else if right-left+1 > max {
			max = right - left + 1
		}
		lastSeen[nextChar] = right
	}
	return max
}
