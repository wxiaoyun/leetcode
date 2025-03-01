package leetcode

import (
  "slices"
)

// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/?envType=daily-question&envId=2023-11-15

func maximumElementAfterDecrementingAndRearranging(arr []int) int {
    slices.Sort(arr)

    if arr[0] != 1 {
        arr[0] = 1
    }

    for i := 1; i < len(arr); i++ {
        if arr[i] - arr[i-1] > 1 { // check if difference larger than 1
            arr[i] = arr[i-1]+1 // decrease value
        }
    }

    return arr[len(arr)-1]
}
