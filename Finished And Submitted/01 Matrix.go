package leetcode

import "math"

// https://leetcode.com/problems/01-matrix/

func updateMatrix(mat [][]int) [][]int {

	var isValid = func(i, j int) bool {
		return i >= 0 && i < len(mat) && j >= 0 && j < len(mat[0])
	}

	directions := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

	// Initialize the datastructures
	result := make([][]int, len(mat))
	for i := range result {
		result[i] = make([]int, len(mat[i]))
		for j := range result[i] {
			if mat[i][j] == 0 {
				result[i][j] = 0
			} else {
				result[i][j] = math.MaxInt
			}

			row, col := i+directions[2][0], j+directions[2][1]
			if isValid(row, col) && result[row][col]+1 < result[i][j] {
				result[i][j] = result[row][col] + 1
			}

			row, col = i+directions[3][0], j+directions[3][1]
			if isValid(row, col) && result[row][col]+1 < result[i][j] {
				result[i][j] = result[row][col] + 1
			}
		}
	}

	for i := range result {
		reverseI := len(result) - 1 - i
		for j := range result[reverseI] {
			reverseJ := len(result[reverseI]) - 1 - j
			row, col := reverseI+directions[0][0], reverseJ+directions[0][1]
			if isValid(row, col) && result[row][col]+1 < result[reverseI][reverseJ] {
				result[reverseI][reverseJ] = result[row][col] + 1
			}

			row, col = reverseI+directions[1][0], reverseJ+directions[1][1]
			if isValid(row, col) && result[row][col]+1 < result[reverseI][reverseJ] {
				result[reverseI][reverseJ] = result[row][col] + 1
			}
		}
	}

	return result
}

func isValid(i, j, rows, cols int) bool {
	return i >= 0 && i < rows && j >= 0 && j < cols
}
