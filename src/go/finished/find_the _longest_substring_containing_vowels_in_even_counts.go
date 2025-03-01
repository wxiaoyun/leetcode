package leetcode

func findTheLongestSubstring(s string) int {
	bitVal := map[rune]int{
		'a': 1,
		'e': 2,
		'i': 4,
		'o': 8,
		'u': 16,
	}

	prev := make([]int, 32)
	for i := range prev {
		prev[i] = -1
	}

	xorMask := 0
	longest := 0
	for i, c := range s {
		xorMask ^= bitVal[c]

		if xorMask == 0 {
			longest = i + 1
			continue
		}

		if prev[xorMask] == -1 {
			prev[xorMask] = i
		}

		longest = max(longest, i-prev[xorMask])
	}

	return longest
}

// func max(a, b int) int {
// 	if a > b {
// 		return a
// 	}
// 	return b
// }

// // Time: O(n^3), brute force
// // space: O(n)
// func findTheLongestSubstring(s string) int {
//     maxLen := 0
//     isVowel := map[byte]bool {
//       'a': true,
//       'e': true,
//       'i': true,
//       'o': true,
//       'u': true,
//     }

//     for i := 0; i < len(s); i++ {
//       for j := i; j < len(s); j++ {
//         tabulate := make(map[byte]int)
//         for k := i; k <= j; k++ {
//           if isVowel[s[k]] {
//             tabulate[s[k]]++
//           }
//         }
//         isValid := true
//         for _, v := range tabulate {
//           if v % 2 != 0 {
//             isValid = false
//             break
//           }
//         }
//         if isValid {
//           maxLen = max(maxLen, j-i+1)
//         }
//       }
//     }
//     return maxLen
// }
