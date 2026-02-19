// https://leetcode.com/problems/count-binary-substrings/

impl Solution {
    pub fn count_binary_substrings(s: String) -> i32 {
        let (mut pcnt, mut ccnt) = (0, 0);
        let mut cur = ' ';

        let mut n_sub = 0;
        for ch in s.chars() {
            if ch != cur {
                cur = ch;
                pcnt = ccnt;
                ccnt = 0;
            }

            ccnt += 1;
            if ccnt <= pcnt {
                n_sub += 1;
            }
        }

        n_sub
    }
}
