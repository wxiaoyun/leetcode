package leetcode

import (
	"sort"
	"strconv"
	"strings"
)

type Wrapper struct {
	S []string
}

func (w Wrapper) Len() int      { return len(w.S) }
func (w Wrapper) Swap(i, j int) { w.S[i], w.S[j] = w.S[j], w.S[i] }
func (w Wrapper) Less(i, j int) bool {
	is, js := w.S[i], w.S[j]
	var1, var2 := is+js, js+is
	return var1 >= var2
}

func largestNumber(nums []int) string {
	numStr := make([]string, 0, len(nums))
	for _, n := range nums {
		numStr = append(numStr, strconv.Itoa(n))
	}

	sort.Sort(Wrapper{numStr})

	resStr := strings.Join(numStr, "")
	if resStr[0] == '0' {
		return "0"
	}

	return resStr
}
