impl Solution {
    pub fn largest_perimeter(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();

        for i in (2..nums.len()).rev() {
            let (a, b, c) = (nums[i], nums[i - 1], nums[i - 2]);
            if b + c > a {
                return a + b + c;
            }
        }

        0
    }
}
