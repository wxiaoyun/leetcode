package leetcode

// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill

func dividePlayers(skill []int) int64 {
	total := 0
	count := make(map[int]int64)

	for _, s := range skill {
		total += s
		if _, ok := count[s]; !ok {
			count[s] = 0
		}
		count[s]++
	}

	pairTotal := total / (len(skill) / 2)

	chemistrySum := int64(0)
	for _, s := range skill {
		if count[s] <= 0 {
			continue
		}

		comp := pairTotal - s
		if c := count[comp]; c <= 0 {
			return -1
		}

		count[s]--
		count[comp]--
		chemistrySum += int64(s * comp)
	}

	return chemistrySum
}
