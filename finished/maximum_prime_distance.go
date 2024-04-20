package leetcode

func maximumPrimeDifference(nums []int) int {
	primes := make([]bool, 101)
	for i := 2; i < len(primes); i++ {
		primes[i] = true
	}

	p := 2
	for p*p < len(primes) {
		if primes[p] {
			for i := p * p; i < len(primes); i += p {
				primes[i] = false
			}
		}
		p += 1
	}

	l, r := 0, len(nums)-1

	for i := l; i <= r; i++ {
		if primes[nums[i]] {
			l = i
			break
		}
	}

	for i := r; i >= l; i-- {
		if primes[nums[i]] {
			r = i
			break
		}
	}

	return r - l
}
