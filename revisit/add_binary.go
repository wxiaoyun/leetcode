package leetcode

import (
	"fmt"
)

// Given two binary strings a and b, return their sum as a binary string.

// Example 1:

// Input: a = "11", b = "1"
// Output: "100"
// Example 2:

// Input: a = "1010", b = "1011"
// Output: "10101"

// Constraints:

// 1 <= a.length, b.length <= 104
// a and b consist only of '0' or '1' characters.
// Each string does not contain leading zeros except for the zero itself.

// https://leetcode.com/problems/add-binary/

func addBinary(a string, b string) string {
	i, j, carry, res := len(a)-1, len(b)-1, 0, ""

	for i >= 0 || j >= 0 {
		sum := carry
		if i >= 0 {
			sum += int(a[i] - '0')
			i--
		}
		if j >= 0 {
			sum += int(b[j] - '0')
			j--
		}
		carry = sum / 2
		res = fmt.Sprintf("%d%s", sum%2, res)
	}
	if carry != 0 {
		res = fmt.Sprintf("1%s", res)
	}
	return res
}
