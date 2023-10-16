package leetcode

// case 1: event1.start <= event1.end < event2.start <= event2.end
// case 1: event2.start <= event2.end < event1.start <= event1.end
func haveConflict(event1 []string, event2 []string) bool {
	if event1[1] < event2[0] {
		return false
	}

	if event2[1] < event1[0] {
		return false
	}

	return true
}
