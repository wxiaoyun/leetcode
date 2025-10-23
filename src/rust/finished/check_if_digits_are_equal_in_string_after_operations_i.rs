impl Solution {
    pub fn has_same_digits(s: String) -> bool {
        let mut digits: Vec<_> = s.chars().map(|ch| ch.to_digit(10).unwrap()).collect();
        let mut bound = digits.len() - 1;

        while bound >= 2 {
            for i in 0..bound {
                digits[i] = (digits[i] + digits[i + 1]).rem_euclid(10);
            }
            bound -= 1;
        }

        digits[0] == digits[1]
    }
}
