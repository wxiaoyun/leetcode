package leetcode

// https://leetcode.com/problems/sentence-similarity-iii

import "strings"

func areSentencesSimilar(sentence1 string, sentence2 string) bool {
	words1, words2 := strings.Split(sentence1, " "), strings.Split(sentence2, " ")
	s1, s2, e1, e2 := 0, 0, len(words1)-1, len(words2)-1

	for s1 < len(words1) && s2 < len(words2) && words1[s1] == words2[s2] {
		s1++
		s2++
	}

	for e1 >= 0 && e2 >= 0 && words1[e1] == words2[e2] {
		e1--
		e2--
	}

	return s1 > e1 || s2 > e2
}

// func areSentencesSimilar(sentence1 string, sentence2 string) bool {
//     words1, words2 := strings.Split(sentence1, " "), strings.Split(sentence2, " ")
//     var longer []string
//     var shorter []string

//     if len(words1) > len(words2) {
//       longer = words1
//       shorter = words2
//     } else {
//       longer = words2
//       shorter = words1
//     }

//     if check(longer, shorter) {
//       return true
//     }

//     slices.Reverse(longer)
//     slices.Reverse(shorter)
//     return check(longer, shorter)
// }

// func check(longer, shorter []string) bool {
//     i := 0
//     j := 0
//     firstBreak := true
//     for i < len(longer) && j < len(shorter) {
//       if longer[i] == shorter[j] {
//         i++
//         j++
//         continue
//       }

//       if !firstBreak {
//         return false
//       }

//       firstBreak = false
//       for i < len(longer) && longer[i] != shorter[j] {
//         i++
//       }

//       i++
//       j++
//     }

//     return j == len(shorter) && (i == len(longer) || firstBreak)
// }
