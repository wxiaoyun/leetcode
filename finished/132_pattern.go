package leetcode

import (
	"math"
)

func find132pattern(nums []int) bool {
	// two is an element in nums each that there exists a greater element ahead
	// it in the slice such that it forms the "32" formation.
	// we want to gradually update two to be larger and larger so that
	// we maximise our chance of finding a "one" that is smaller than "two"
	two := math.MinInt
	stack := []int{} // stack of potential "two"s

	for i := len(nums) - 1; i >= 0; i-- {
		num := nums[i]
		// if we found a num that is greater than two, then the 132 formation is found
		if num < two {
			return true
		}

		// num >= two
		// now we try to increase "two"
		for len(stack) > 0 && stack[len(stack)-1] < num {
			// update two to a bigger number where the "3, 2" pattern is "num, stack[len(stack)-1]"
			two = stack[len(stack)-1] // stack[len(stack) - 1] > num >= two

			// since stack[:len(stack)-1] is already two, we remove it from the potential "two"s
			stack = stack[:len(stack)-1] // pop the stack
		}
		// add the current number into the stack of numbers we have encountered
		stack = append(stack, num)
	}

	// if no 132 pattern is found by this point, this pattern does not exist
	return false
}
