package leetcode

// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

import "strconv"

func longestCommonPrefix(arr1 []int, arr2 []int) int {
	trie1 := newtrie()
	for _, n1 := range arr1 {
		trie1.insert(strconv.Itoa(n1))
	}

	maxLen := -1

	for _, n2 := range arr2 {
		maxLen = max(
			maxLen,
			trie1.longestPrefix(strconv.Itoa(n2)),
		)
	}

	return maxLen
}

type trie struct {
	isEnd    bool
	children []*trie
}

func newtrie() *trie {
	return &trie{
		children: make([]*trie, 10),
	}
}

func (t *trie) insert(s string) {
	if s == "" {
		t.isEnd = true
		return
	}

	c := int(s[0] - '0')
	rest := s[1:]

	if t.children[c] == nil {
		t.children[c] = newtrie()
	}
	t.children[c].insert(rest)
}

func (t *trie) longestPrefix(s string) int {
	if s == "" {
		return 0
	}

	c := int(s[0] - '0')
	rest := s[1:]

	if t.children[c] == nil {
		return 0
	}

	return 1 + t.children[c].longestPrefix(rest)
}
