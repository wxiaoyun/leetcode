package leetcode

// You are climbing a staircase. It takes n steps to reach the top.

// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

// Example 1:

// Input: n = 2
// Output: 2
// Explanation: There are two ways to climb to the top.
// 1. 1 step + 1 step
// 2. 2 steps
// Example 2:

// Input: n = 3
// Output: 3
// Explanation: There are three ways to climb to the top.
// 1. 1 step + 1 step + 1 step
// 2. 1 step + 2 steps
// 3. 2 steps + 1 step

// Constraints: 1 <= n <= 45

// https://leetcode.com/problems/climbing-stairs/

func climbStairs(n int) int {
	prevPrev := 1
	prev := 1

	for i := 2; i <= n; i++ {
		this := prevPrev + prev
		prevPrev, prev = prev, this
	}

	return prev
}

// func climbStairs(n int) int {
// 	return helper4(make([]int, n+1), n)
// }

// func helper4(memo []int, n int) int {
// 	if n <= 2 {
// 		return n
// 	}

// 	// Yet to be calculated
// 	if memo[n] == 0 {
// 		result := helper4(memo, n-1) + helper4(memo, n-2)
// 		memo[n] = result
// 		return result
// 	}
// 	return memo[n]
// }
