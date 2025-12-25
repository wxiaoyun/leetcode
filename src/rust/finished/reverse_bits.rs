impl Solution {
    pub fn reverse_bits(n: i32) -> i32 {
        let mut n = n;
        let mut ans = 0;
        for _ in 0..32 {
            ans = (ans << 1) + (n & 1);
            n >>= 1;
        }
        ans
    }
}
