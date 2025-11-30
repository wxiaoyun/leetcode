impl Solution {
    pub fn min_subarray(nums: Vec<i32>, p: i32) -> i32 {
        let target = nums
            .iter()
            .copied()
            .fold(0, |acc, n| (acc + n).rem_euclid(p));
        if target == 0 {
            return 0;
        }

        let mut last_seen = std::collections::HashMap::from([(0, -1)]);
        let n = nums.len() as i32;
        let mut cur = 0;
        let mut best = n;
        for (i, n) in nums.into_iter().enumerate() {
            let i = i as i32;
            cur = (cur + n).rem_euclid(p);
            let need = (cur - target).rem_euclid(p);
            match last_seen.get(&need) {
                Some(&j) => best = best.min(i - j),
                _ => (),
            };
            last_seen.insert(cur, i);
        }

        if best < n {
            best
        } else {
            -1
        }
    }
}
