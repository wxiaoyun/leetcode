package leetcode

import "math"

// import "fmt"

// func reverse(x int) int {
// 	if x < 0 {
// 		return -1 * reverse(-x)
// 	}

// 	if x < 10 {
// 		return x
// 	}

// 	result := 0
// 	remaining := x
// 	for divisor := 10; divisor/10 < x; divisor *= 10 {
// 		result = result*10 + remaining%divisor/(divisor/10)
// 		fmt.Println(remaining, result)
// 		remaining -= remaining % divisor
// 	}
// 	return result
// }

func reverse(x int) int {
	result := 0
	if x < 0 {
		result = -1 * helper1(0, -x)
	} else {
		result = helper1(0, x)
	}

	if result < int(-math.Pow(2, 31)) || result > int(math.Pow(2, 31))-1 {
		return 0
	}
	return result
}

func helper1(accum int, remaining int) int {
	if remaining < 10 {
		return accum*10 + remaining
	}

	return helper1(accum*10+remaining%10, remaining/10)
}
