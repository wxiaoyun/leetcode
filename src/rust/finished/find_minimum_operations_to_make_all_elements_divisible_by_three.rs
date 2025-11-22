impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        nums.into_iter()
            .map(|n| n.rem_euclid(3).min(3 - n.rem_euclid(3)))
            .sum()
    }
}
