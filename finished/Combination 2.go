package leetcode

import (
	"sort"
	"strconv"
	"strings"
)

func combinationSum2(candidates []int, target int) [][]int {
	dp := make([]map[string]bool, target+1)
	dp[0] = map[string]bool{"": true}
	for i := 1; i <= target; i++ {
		dp[i] = make(map[string]bool)
	}

	sort.Ints(candidates)

	for _, cand := range candidates {
		for i := target; i >= cand; i-- { // Note the reverse order here
			for k := range dp[i-cand] {
				comb := deserialize(k)
				comb = append(comb, cand)
				sort.Ints(comb)
				dp[i][serialize(comb)] = true
			}
		}
	}

	result := [][]int{}
	for k := range dp[target] {
		result = append(result, deserialize(k))
	}

	return result
}

func serialize(comb []int) string {
	strs := []string{}
	for _, num := range comb {
		strs = append(strs, strconv.Itoa(num))
	}
	return strings.Join(strs, ",")
}

func deserialize(s string) []int {
	strs := strings.Split(s, ",")
	var comb []int
	for _, str := range strs {
		if str == "" {
			continue
		}
		num, _ := strconv.Atoi(str)
		comb = append(comb, num)
	}
	return comb
}
