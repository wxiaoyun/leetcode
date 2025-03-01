struct Solution;

impl Solution {
    pub fn maximum_prime_difference(nums: Vec<i32>) -> i32 {
        let mut primes = [true; 101];
        primes[0] = false;
        primes[1] = false;

        let mut i = 2;

        while i * i < primes.len() {
            if primes[i] {
                let mut p = i * i;

                while p < primes.len() {
                    primes[p] = false;
                    p += i;
                }
            }

            i += 1;
        }

        let mut found_left = false;
        let mut left = 0;
        let mut right = 0;

        nums.iter().enumerate().for_each(|(i, n)| {
            if primes[*n as usize] {
                if !found_left {
                    left = i;
                    found_left = true;
                }
                right = i;
            }
        });

        return (right - left) as i32;
    }
}
