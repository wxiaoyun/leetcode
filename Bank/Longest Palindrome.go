package leetcode

// Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

// Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

// Example 1:

// Input: s = "abccccdd"
// Output: 7
// Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
// Example 2:

// Input: s = "a"
// Output: 1
// Explanation: The longest palindrome that can be built is "a", whose length is 1.

// Constraints:

// 1 <= s.length <= 2000
// s consists of lowercase and/or uppercase English letters only.

// https://leetcode.com/problems/longest-palindrome/

// func longestPalindrome(s string) int {
// 	charFrequency := make(map[rune]int)

// 	for _, char := range s {
// 		charFrequency[char]++
// 	}

// 	hasSeenOdd := false
// 	length := 0

// 	for _, freq := range charFrequency {
// 		if freq%2 == 0 {
// 			length += freq
// 			continue
// 		}

// 		if !hasSeenOdd {
// 			length += freq
// 			hasSeenOdd = true
// 		} else {
// 			length += freq - 1
// 		}

// 	}

// 	return length
// }

func longestPalindrome(s string) int {
	charFrequency := make([]int, 'z'-'a'+1+'Z'-'A'+1)

	for _, char := range s {
		charFrequency[charToIndex(int(char))]++
	}

	hasSeenOdd := false
	length := 0

	for _, freq := range charFrequency {
		if freq%2 == 0 {
			length += freq
			continue
		}

		if !hasSeenOdd {
			length += freq
			hasSeenOdd = true
		} else {
			length += freq - 1
		}

	}

	return length
}

func charToIndex(char int) int {
	if char >= 'A' && char <= 'Z' {
		return char - 'A'
	}
	if char >= 'a' && char <= 'z' {
		return char - 'a' + ('Z' - 'A' + 1)
	}
	return -1
}
