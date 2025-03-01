package leetcode

// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

// O(nk), k = avg str len
func sumPrefixScores(words []string) []int {
	answers := make([]int, len(words))

	t := newSPSTrie()
	for _, w := range words {
		t.insert(w)
	}

	for i, w := range words {
		answers[i] = t.prefixCount(w)
	}

	return answers
}

type SPStrie struct {
	isEnd    bool
	count    int
	children []*SPStrie
}

func newSPSTrie() *SPStrie {
	return &SPStrie{
		children: make([]*SPStrie, 26),
	}
}

func (t *SPStrie) insert(s string) {
	if s == "" {
		t.isEnd = true
		return
	}

	c := int(s[0] - 'a')
	rem := s[1:]

	if t.children[c] == nil {
		t.children[c] = newSPSTrie()
	}

	t.children[c].count++
	t.children[c].insert(rem)
}

func (t *SPStrie) prefixCount(s string) int {
	if s == "" {
		return t.count
	}

	c := int(s[0] - 'a')
	rem := s[1:]

	if t.children[c] == nil {
		return 0
	}

	return t.count + t.children[c].prefixCount(rem)
}
