impl Solution {
    pub fn find_final_value(nums: Vec<i32>, original: i32) -> i32 {
        let seen: std::collections::HashSet<i32> = nums.into_iter().collect();
        let mut target = original;
        while seen.contains(&target) {
            target <<= 1;
        }
        target
    }
}
