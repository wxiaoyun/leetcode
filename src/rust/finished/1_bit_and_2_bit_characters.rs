impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        let mut i = 0_usize;
        let n = bits.len();
        while i < n - 1 {
            match bits[i] {
                0 => i += 1,
                1 => i += 2,
                _ => unreachable!(),
            }
        }
        i == n - 1
    }
}
