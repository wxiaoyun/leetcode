impl Solution {
    pub fn max_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let k = k as usize;
        let mut bests = vec![i32::MIN as i64; k];
        let mut best = i64::MIN;
        let mut acc = 0i64;
        for (i, &n) in nums.iter().enumerate() {
            acc += n as i64;
            if i >= k {
                acc -= nums[i - k] as i64;
            }
            if i >= k - 1 {
                let j = i.rem_euclid(k);
                bests[j] = acc.max(bests[j] + acc);
                best = best.max(bests[j])
            }
        }
        best
    }
}
