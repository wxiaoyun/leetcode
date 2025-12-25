impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let is_neg = x < 0;
        let mut x = if is_neg { -x } else { x };
        let mut ans = 0i32;
        while x != 0 {
            let Some(ok) = ans.checked_mul(10).and_then(|ans| ans.checked_add(x % 10)) else {
                return 0;
            };
            ans = ok;
            x /= 10;
        }
        if is_neg {
            -ans
        } else {
            ans
        }
    }
}
