// https://leetcode.com/problems/maximum-odd-binary-number/description/

impl Solution {
    pub fn maximum_odd_binary_number(s: String) -> String {
        let mut one_count = 0;

        s.chars().for_each(|c| {
            if c == '1' {
                one_count += 1;
            }
        });

        let mut result = String::new();
        result.reserve(s.len());

        let zero_count = s.len() - one_count;

        for _ in (0..one_count - 1) {
            result.push_str("1");
        }

        for _ in (0..zero_count) {
            result.push_str("0");
        }

        result.push_str("1");

        result
    }
}
