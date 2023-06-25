package leetcode

import "fmt"

func isValidSudoku(board [][]byte) bool {
	for i := 0; i < 9; i++ {
		if !isValidRow(board, i) {
			return false
		}
		if !isValidCol(board, i) {
			return false
		}
		if !isValidBox(board, i) {
			return false
		}
	}
	return true
}

var byteToNum = map[byte]int{
	'0': 0,
	'1': 1,
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'.': -1,
}

func isValidRow(board [][]byte, row int) bool {
	seen := make([]bool, 10)
	fmt.Println(seen)

	for _, byte := range board[row] {
		if byteToNum[byte] < 0 {
			continue
		}
		if seen[byteToNum[byte]] {

			return false
		}
		seen[byteToNum[byte]] = true
	}
	return true
}

func isValidCol(board [][]byte, col int) bool {
	seen := make([]bool, 10)
	for _, row := range board {
		if byteToNum[row[col]] < 0 {
			continue
		}
		if seen[byteToNum[row[col]]] {
			return false
		}
		seen[byteToNum[row[col]]] = true
	}
	return true
}

func isValidBox(board [][]byte, box int) bool {
	seen := make([]bool, 10)
	row := box / 3
	col := box % 3
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if byteToNum[board[i+row*3][j+col*3]] < 0 {
				continue
			}
			if seen[byteToNum[board[i+row*3][j+col*3]]] {
				return false
			}
			seen[byteToNum[board[i+row*3][j+col*3]]] = true
		}
	}
	return true
}
