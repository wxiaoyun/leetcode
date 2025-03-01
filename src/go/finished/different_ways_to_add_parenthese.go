package leetcode

import (
	"fmt"
	"strconv"
)

func diffWaysToCompute(exp string) []int {
	if len(exp) <= 2 {
		num, _ := strconv.Atoi(exp)
		return []int{num}
	}

	res := []int{}

	for i, c := range exp {
		switch c {
		case '+':
			fallthrough
		case '-':
			fallthrough
		case '*':
			res = append(res, helperDiff(exp[:i], exp[i:i+1], exp[i+1:])...)
		default:
			continue
		}
	}

	return res
}

func helperDiff(a string, op string, b string) []int {
	aNum := []int{}
	if len(a) <= 2 {
		num, _ := strconv.Atoi(a)
		aNum = append(aNum, num)
	} else {
		aNum = diffWaysToCompute(a)
	}

	bNum := []int{}
	if len(b) <= 2 {
		num, _ := strconv.Atoi(b)
		bNum = append(bNum, num)
	} else {
		bNum = diffWaysToCompute(b)
	}

	res := make([]int, 0, len(aNum)*len(bNum))
	for i := range aNum {
		for j := range bNum {
			calc := 0
			switch op {
			case "+":
				calc = aNum[i] + bNum[j]
			case "-":
				calc = aNum[i] - bNum[j]
			case "*":
				calc = aNum[i] * bNum[j]
			default:
				panic(fmt.Sprintf("Invalid operator: %s", op))
			}
			res = append(res, calc)
		}
	}

	return res
}
