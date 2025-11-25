impl Solution {
    pub fn smallest_repunit_div_by_k(k: i32) -> i32 {
        let mut rems = vec![false; k as usize];
        let mut rem_mod_k = 0i32;
        let mut i = 0;
        loop {
            rem_mod_k = (rem_mod_k * 10 + 1).rem_euclid(k);
            if rem_mod_k == 0 {
                return i + 1;
            }
            if rems[rem_mod_k as usize] {
                return -1;
            }
            rems[rem_mod_k as usize] = true;
            i += 1;
        }
    }
}
