impl Solution {
    pub fn count_partitions(nums: Vec<i32>) -> i32 {
        let total: i32 = nums.iter().sum();
        let mut cur: i32 = 0;
        let mut count = 0;
        for n in nums.iter().take(nums.len() - 1) {
            cur += n;
            if (total - cur * 2).rem_euclid(2) == 0 {
                count += 1;
            }
        }
        count
    }
}
