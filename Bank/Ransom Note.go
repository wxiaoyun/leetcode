package leetcode

// Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

// Each letter in magazine can only be used once in ransomNote.

// Example 1:

// Input: ransomNote = "a", magazine = "b"
// Output: false
// Example 2:

// Input: ransomNote = "aa", magazine = "ab"
// Output: false
// Example 3:

// Input: ransomNote = "aa", magazine = "aab"
// Output: true

// Constraints:

// 1 <= ransomNote.length, magazine.length <= 105
// ransomNote and magazine consist of lowercase English letters.

// https://leetcode.com/problems/ransom-note/

func canConstruct(ransomNote string, magazine string) bool {
	if len(ransomNote) > len(magazine) {
		return false
	}

	freqArr := make([]int, 'z'-'a'+1)
	for _, char := range magazine {
		freqArr[int(char)-'a']++
	}
	for _, char := range ransomNote {
		freqArr[int(char)-'a']--
		if freqArr[int(char)-'a'] < 0 {
			return false
		}
	}
	// for _, freq := range freqArr {
	// 	if freq < 0 {
	// 		return false
	// 	}
	// }

	return true
}
