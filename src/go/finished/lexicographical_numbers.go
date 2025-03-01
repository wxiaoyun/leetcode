package leetcode

// https://leetcode.com/problems/lexicographical-numbers/

func lexicalOrder(n int) []int {
	var dfs func(int, []int) []int
	dfs = func(prefix int, res []int) []int {
		if prefix > n {
			return res
		}

		res = append(res, prefix)
		for i := 0; i < 10; i++ {
			res = dfs(prefix*10+i, res)
		}
		return res
	}

	res := make([]int, 0, n)
	for i := 1; i < 10; i++ {
		res = dfs(i, res)
	}
	return res
}

// func lexicalOrder(n int) []int {
// 	tmp := []string{}
// 	for i := 1; i <= n; i++ {
// 		tmp = append(tmp, strconv.Itoa(i))
// 	}

// 	t := newTrie()
// 	for _, num := range tmp {
// 		t.Insert(num)
// 	}

// 	return list(t)
// }

// type LNTrie struct {
// 	IsEnd    bool
// 	Children []*LNTrie
// }

// func newTrie() *LNTrie {
// 	return &LNTrie{
// 		Children: make([]*LNTrie, 10),
// 	}
// }

// func (t *LNTrie) Insert(s string) {
// 	if s == "" {
// 		t.IsEnd = true
// 		return
// 	}

// 	c := int(s[0] - '0')
// 	rest := s[1:]

// 	if st := t.Children[c]; st == nil {
// 		t.Children[c] = newTrie()
// 	}

// 	t.Children[c].Insert(rest)
// }

// func list(t *LNTrie) []int {
// 	var helper func(*LNTrie, int, []int) []int
// 	helper = func(t *LNTrie, accum int, res []int) []int {
// 		if t.IsEnd {
// 			res = append(res, accum)
// 		}

// 		for num, st := range t.Children {
// 			if st == nil {
// 				continue
// 			}
// 			res = helper(st, accum*10+num, res)
// 		}

// 		return res
// 	}

// 	return helper(t, 0, []int{})
// }
