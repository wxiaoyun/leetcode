// https://leetcode.com/problems/binary-number-with-alternating-bits

impl Solution {
    pub fn has_alternating_bits(n: i32) -> bool {
        let mut cur = n;
        let mut prev = (cur & 1) ^ 1;
        while cur != 0 {
            if (cur & 1) == prev {
                return false;
            }
            prev = (cur & 1);
            cur >>= 1;
        }

        true
    }
}
