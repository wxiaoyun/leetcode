impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in 0..=nums.len() {
            ans ^= i as i32;
            if i < nums.len() {
                ans ^= nums[i];
            }
        }
        ans
    }
}
