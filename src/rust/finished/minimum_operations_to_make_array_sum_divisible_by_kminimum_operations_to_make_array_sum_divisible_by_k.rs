impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        nums.into_iter().fold(0, |acc, n| (acc + n).rem_euclid(k))
    }
}
