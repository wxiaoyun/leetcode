impl Solution {
    pub fn prefixes_div_by5(nums: Vec<i32>) -> Vec<bool> {
        let mut acc = 0;
        let mut ans = Vec::with_capacity(nums.len());
        for n in nums.into_iter() {
            acc = (acc << 1) + n;
            acc = acc.rem_euclid(5);
            ans.push(acc == 0)
        }
        ans
    }
}
