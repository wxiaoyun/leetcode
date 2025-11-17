impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let mut last_seen: i32 = -k - 1;
        for (i, &n) in nums.iter().enumerate() {
            if n != 1 {
                continue;
            }

            let i = i as i32;
            if i - last_seen <= k {
                return false;
            }

            last_seen = i;
        }

        true
    }
}
