package leetcode

import (
	"fmt"
	"math"
)

func generateMatrix(n int) [][]int {
	output := make([][]int, n)
	for i, _ := range output {
		output[i] = make([]int, n)
	}

	left := 0
	right := n - 1
	top := 1
	bottom := n - 1

	const (
		rightwards = iota
		downwards
		leftwards
		upwards
	)

	index1, index2 := 0, 0

	currDir := rightwards
	for count := 1; count <= int(math.Pow(float64(n), 2)); count++ {
		output[index1][index2] = count
		fmt.Printf("Curr Dir: %v, count: %v, r: %v, c: %v\n", currDir, count, index1, index2)

		switch currDir {
		case rightwards:
			if index2 == right {
				right--
				currDir = downwards
				index1++
			} else {
				index2++
			}
		case downwards:
			if index1 == bottom {
				bottom--
				currDir = leftwards
				index2--
			} else {
				index1++
			}
		case leftwards:
			if index2 == left {
				left++
				currDir = upwards
				index1--
			} else {
				index2--
			}
		case upwards:
			if index1 == top {
				top++
				currDir = rightwards
				index2++
			} else {
				index1--
			}
		}
	}

	return output
}
