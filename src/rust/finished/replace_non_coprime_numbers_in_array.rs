impl Solution {
    pub fn replace_non_coprimes(nums: Vec<i32>) -> Vec<i32> {
        #[inline(always)]
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b > 0 {
                let tmp = a;
                a = b;
                b = tmp % b;
            }
            a
        }

        nums.iter().fold(Vec::new(), |mut prev_nums, &n| {
            let mut cur = n;
            while let Some(&prev_n) = prev_nums.last() {
                match gcd(prev_n, cur) {
                    1 => break,
                    gcd_num => {
                        cur = cur / gcd_num * prev_nums.pop().unwrap();
                    }
                }
            }
            prev_nums.push(cur);
            prev_nums
        })
    }
}
