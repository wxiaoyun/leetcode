impl Solution {
    pub fn special_triplets(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let total_occurrence =
            nums.iter()
                .copied()
                .fold(std::collections::HashMap::new(), |mut mp, n| {
                    *mp.entry(n).or_insert(0) += 1;
                    mp
                });

        let mut prev_occurrence = std::collections::HashMap::new();
        let mut ans = 0;
        for n in nums {
            let n2 = n * 2;
            let prev_cnt = prev_occurrence.get(&n2).copied().unwrap_or(0);
            let mut post_cnt = total_occurrence.get(&n2).copied().unwrap_or(0) - prev_cnt;
            if n == n2 {
                post_cnt -= 1;
            }
            ans = (ans + prev_cnt * post_cnt) % MOD;
            *prev_occurrence.entry(n).or_insert(0) += 1;
        }

        ans as i32
    }
}
