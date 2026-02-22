impl Solution {
    pub fn binary_gap(n: i32) -> i32 {
        let mut prev_one_idx = 1 << 16;
        let mut cur_idx = 0;

        let mut best = 0;
        let mut cur = n;
        while cur != 0 {
            let bit = cur & 1;
            cur >>= 1;

            if bit == 1 {
                best = best.max(cur_idx - prev_one_idx);
                prev_one_idx = cur_idx;
            }

            cur_idx += 1;
        }

        best
    }
}
