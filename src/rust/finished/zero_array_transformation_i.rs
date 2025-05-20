// https://leetcode.com/problems/zero-array-transformation-i

impl Solution {
    pub fn is_zero_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> bool {
        let n = nums.len();
        let mut prefix_delta = vec![0; n + 1];

        for q in queries.iter() {
            let l = q[0] as usize;
            let r = q[1] as usize;
            prefix_delta[l] -= 1;
            if r + 1 < n + 1 {
                prefix_delta[r + 1] += 1;
            }
        }

        let mut cur_delta = 0;
        for i in 0..n {
            cur_delta += prefix_delta[i];
            if (nums[i] + cur_delta) > 0 {
                return false;
            }
        }

        true
    }
}
