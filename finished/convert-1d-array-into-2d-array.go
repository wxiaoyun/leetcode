package leetcode

// https://leetcode.com/problems/convert-1d-array-into-2d-array

func construct2DArray(original []int, m int, n int) [][]int {
	res := [][]int{}
	if len(original) != m*n {
		return res
	}

	for i := 0; i < m; i++ {
		row := []int{}
		for j := 0; j < n; j++ {
			row = append(row, original[i*n+j])
		}
		res = append(res, row)
	}

	return res
}
