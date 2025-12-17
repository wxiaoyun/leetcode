impl Solution {
    pub fn maximum_sum(arr: Vec<i32>) -> i32 {
        let mut ans = i32::MIN / 2;
        let mut best = i32::MIN / 2;
        let mut best_del = i32::MIN / 2;
        for n in arr {
            best_del = best.max(best_del + n);
            best = n.max(best + n);
            ans = ans.max(best).max(best_del);
        }
        ans
    }
}
