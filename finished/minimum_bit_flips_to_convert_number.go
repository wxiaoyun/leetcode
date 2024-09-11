package leetcode

// https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

func minBitFlips(start int, goal int) int {
	xor := start ^ goal

	flips := 0
	for xor != 0 {
		flips += xor & 1
		xor = xor >> 1
	}

	return flips
}

// func minBitFlips(start int, goal int) int {
//   startBits := bitVal(start)
//   goalBits := bitVal(goal)

//   flips := 0
//   for i := 0; i < 32; i++ {
//     if startBits[i] != goalBits[i] {
//       flips++
//     }
//   }

//   return flips
// }

// func bitVal(a int) [32]bool {
//   res := [32]bool{}

//   for i := 31; i >= 0; i-- {
//     if a <= 0 {
//       break
//     }

//     qtn := a / 2
//     rmd := a % 2
//     res[i] = rmd != 0
//     a = qtn
//   }

//   return res
// }
