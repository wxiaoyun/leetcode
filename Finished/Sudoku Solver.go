package leetcode

// https://leetcode.com/problems/sudoku-solver/

// var byteToNum = map[byte]int{
// 	'0': 0,
// 	'1': 1,
// 	'2': 2,
// 	'3': 3,
// 	'4': 4,
// 	'5': 5,
// 	'6': 6,
// 	'7': 7,
// 	'8': 8,
// 	'9': 9,
// 	'.': -1,
// }

func numToByte(num int) byte {
	return byte(num + 48)
}

// returns the valid numbers that can be placed at the given row and col
func getValidNums(board [][]byte, row, col int) []byte {
	validNums := []byte{'.'}

	// 1-9 are valid
	for i := 1; i <= 9; i++ {
		validNums = append(validNums, numToByte(i))
	}

	for i := 0; i < 9; i++ {
		if board[row][i] != '.' {
			validNums[byteToNum[board[row][i]]] = '.'
		}
		if board[i][col] != '.' {
			validNums[byteToNum[board[i][col]]] = '.'
		}
	}

	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			rowIndex := row - row%3 + i
			colIndex := col - col%3 + j
			if board[rowIndex][colIndex] != '.' {
				validNums[byteToNum[board[rowIndex][colIndex]]] = '.'
			}
		}
	}

	return validNums
}

// func isValidRow(board [][]byte, row int) bool {
// 	seen := make([]bool, 10)

// 	for _, byte := range board[row] {
// 		if byteToNum[byte] < 0 {
// 			continue
// 		}
// 		if seen[byteToNum[byte]] {

// 			return false
// 		}
// 		seen[byteToNum[byte]] = true
// 	}
// 	return true
// }

// func isValidCol(board [][]byte, col int) bool {
// 	seen := make([]bool, 10)
// 	for _, row := range board {
// 		if byteToNum[row[col]] < 0 {
// 			continue
// 		}
// 		if seen[byteToNum[row[col]]] {
// 			return false
// 		}
// 		seen[byteToNum[row[col]]] = true
// 	}
// 	return true
// }

// func isValidBox(board [][]byte, box int) bool {
// 	seen := make([]bool, 10)
// 	row := box / 3
// 	col := box % 3
// 	for i := 0; i < 3; i++ {
// 		for j := 0; j < 3; j++ {
// 			if byteToNum[board[i+row*3][j+col*3]] < 0 {
// 				continue
// 			}
// 			if seen[byteToNum[board[i+row*3][j+col*3]]] {
// 				return false
// 			}
// 			seen[byteToNum[board[i+row*3][j+col*3]]] = true
// 		}
// 	}
// 	return true
// }

func isValidMove(board [][]byte, row, col int, entry byte) bool {
	board[row][col] = entry
	valid := isValidRow(board, row) && isValidCol(board, col) && isValidBox(board, row/3*3+col/3)
	board[row][col] = '.'
	return valid
}

func solve(board [][]byte, row, col int) bool {
	// Gradually fill in the board from left to right, top to bottom
	if col == 9 {
		col = 0
		row++
	}

	// If we've reached the end of the board, we're done
	if row == 9 {
		return true
	}

	// If the current cell is already filled, move on to the next one
	if board[row][col] != '.' {
		return solve(board, row, col+1)
	}

	// Try all valid numbers for the current cell
	for _, num := range getValidNums(board, row, col) {
		if num == '.' {
			continue
		}
		board[row][col] = num
		// If we've solved the board, we're done
		if solve(board, row, col+1) {
			return true
		}
	}
	// If we've tried all valid numbers and none of them worked, backtrack
	board[row][col] = '.'
	return false
}

func solveSudoku(board [][]byte) {
	solve(board, 0, 0)
}
